# def climbStairs(n):
#     if n == 0 or n == 1:
#         return 1

#     first = 1  # ways to reach step 0
#     second = 1  # ways to reach step 1

#     for i in range(2, n + 1):
#         third = first + second
#         first = second
#         second = third

#     return second

# print(climbStairs(5))

