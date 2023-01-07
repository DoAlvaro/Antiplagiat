import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Antiplagiat')
parser.add_argument('input', type=str, help='Input file')
parser.add_argument('output', type=str, help='Output file')
args = parser.parse_args()

def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

input_file = open("input.txt")
with open("scores.txt", 'w+') as output_file:
    space = input_file.readlines()
    for current_files in space:
        first,second = map(str,current_files.split())
        first_file = open(first).read()
        second_file = open(second).read()
        output_file.write(str(np.round(levenstein(first_file, second_file) / len(first_file), 3)) + '\n')
