# Taking Input
# String Input and Print: Read a string s (which may contain spaces) and print it as it is.
# Integer Input and Print: Read an integer n and print it without any change.
# Float Input and floor Print: Read a floating-point number as input, take its floor value, and print as an integer.
# Examples:

# Input: s = "Hello", n = 20, f = 5.5
# Output: 
# Hello
# 20
# 5
# Explanation: 
# The string Hello is printed as it is.
# The integer 20 is printed without any change.
# For floating-point number 5.5, its floor value 5 is printed.

import math

# s to store string
# n to store integer
# f to store float
# ff  # To Store floor of float variable f

###
import math
s = input()
n = int(input())
f = float(input())

ff = math.floor(f)

print(s)
print(n)
print(ff)
