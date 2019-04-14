# coding=utf-8
# 读取文件

from sys import argv

script, filename = argv

txt = open(filename, encoding="utf-8")

print(f"Here is your file {filename}:")
print(txt.read())

print("Type your file again:")
file_again = input("> ")

txt_again = open(file_again, encoding="utf-8")

print(txt_again.read())
