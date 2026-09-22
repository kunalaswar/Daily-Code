# Decision Making
# Given two integers, n and m. The task is to check the relation between n and m. Print "less" if n < m,  "equal" if n == m, and "greater" if n > m.

# Examples :
# Input: n = 4, m = 8
# Output: less
# Explanation: 4 < 8 so print 'less'.
# Input: n = 8, m = 8
# Output: equal
# Explanation: 8 = 8 so print 'equal'.
# Input: n = 8, m = 4
# Output: greater
# Explanation: 8 > 4 so print 'greater'

###
n = int(input())
m = int(input())
if n < m:
    print("less")
elif n == m:
    print("equal")
else:
    print("greater")
