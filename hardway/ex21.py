# coding=utf-8
# 函数返回值

def add(a, b):
  print(f"ADDING {a} + {b}")
  return a + b

def subtract(a, b):
  print(f"SBUTRACTING {a} - {b}")
  return a - b

def multiply(a, b):
  print(f"MULTIPLYING {a} * {b}")
  return a * b

def divide(a, b):
  print(f"DIVIDING {a} / {b}")
  return a / b

print("Let's do some math with these functions:")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# do some complex operations
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
