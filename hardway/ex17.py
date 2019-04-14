# coding=utf-8

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file, encoding="utf-8")
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long.")

print(f"Does the output file exists? {exists(to_file)}")

print("Ready! Hit Enter to continue, and CTRL+C to abort.")
input()

out_file = open(to_file, "w+", encoding="utf-8")
out_file.write(in_data)

print("Alright, all done.")

out_file.close()
in_file.close()

'''
命令行里面运行：
python hardway/ex17.py hardway/ex16_file.txt hardway/ex17_file.txt

'''

