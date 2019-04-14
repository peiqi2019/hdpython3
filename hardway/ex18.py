# coding=utf-8
# 函数定义与调用

def print_two(*args):
  arg1, arg2 = args
  print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
  print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
  print(f"arg1: {arg1}")

def print_none():
  print("I got nothing.")

print_two("Come on", "Baby")
print_two_again("Come on", "Baby")
print_one("The only arg")
print_none()

