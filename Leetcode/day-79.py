
# 746. Min Cost Climbing Stairs

# def minCostClimbingStairs(cost):
#     prev1 = 0  # cost to reach the step just before current
#     prev2 = 0  # cost to reach two steps before current

#     for c in cost:
#         curr = c + min(prev1, prev2)  # pay current step + cheaper of last two
#         prev2, prev1 = prev1, curr   # shift for next step

#     return min(prev1, prev2)  # choose the cheaper way to reach the top

# print(minCostClimbingStairs([10, 15, 20]))  

# print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  

