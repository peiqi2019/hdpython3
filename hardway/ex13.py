# coding=utf-8
# 参数，解包以及变量

from sys import argv

script, first, second, third = argv

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

# 命令行里面这样运行：
# python hardway/ex13.py first second thd
# python hardway/ex13.py 1 2 3
# python hardway/ex13.py a b c
# python hardway/ex13.py 1 a first

