# coding=utf-8
# 读写文件

"""
open: 打开文件获取文件的操作句柄（句柄就是指向文件的标记）
close: 关闭文件
read: 读取整个文件
readline: 读取一行
truncate: 清空文件，使用要注意
write("stuff"): 将"stuff"写入文件
seek(0): 将读写指针移到文件开头
seek(100): 将读写指针移到文件开头起第100个字符的位置
"""

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w', encoding="utf-8")

print("Truncate the file. Goodbye!")
target.truncate()

print("Now i am going to ask you input three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I am goint to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close the file.")
target.close()

"""
创建一个 hardway/ex16_file.txt 文件，随便输入一些内容
命令行运行：python hardway/ex16.py hardway/ex16_file.txt


open(file, mode), mode 包括以下几种：
r   只读
r+  读写
w   写入，先删除原文件，再重新创建并写入，若文件不存在则创建
w+  读写，先删除原文件，再重新创建并写入，若文件不存在则创建
a   写入，在文件末尾追加新内容，若文件不存在则创建
a+  读写，在文件末尾追加新内容，若文件不存在则创建
b   打开二进制文件，可与r,w,a,+结合使用，如：wb+
U   支持所有换行符：\r, \n, \r\n，可与r,w,a,+结合，但必须以r开头，如'rUa+', 'rUw+'

"""
