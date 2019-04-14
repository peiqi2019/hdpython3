# coding=utf-8

from sys import argv

script, input_file = argv

def print_all(f):
  print(f.read())

def rewind(f):
  f.seek(0)


def print_a_line(line_count, f):
  print(line_count, f.readline())

current_file = open(input_file, encoding="utf-8")

prinf("First, let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

'''
命令行里面运行：
python hardway/ex20.py hardway/ex16_file.txt

'''

