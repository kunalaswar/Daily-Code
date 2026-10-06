#Last Digit of Number

# Given an integer n. Write a program to print the last digit of n.

# Examples:

# Input: n = 10
# Output: 0
# Input: n = 9768
# Output: 8

n = int(input())

# code here
print(abs(n) % 10)