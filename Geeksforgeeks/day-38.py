# Mega Sale

class Solution:
    def maxProfit(self,m, arr):
        
        lst = [i for i in arr if i<0]
        lst.sort()


        s  = 0
        for i in range(min(m, len(lst))):
            s += abs(lst[i])
        return s


m = 3
arr = [-6, 0, 35, 4]
s = Solution()
res = s.maxProfit(m,arr)
print(f"Maximun profit of useless laptop is {m} : {res}")

m = 2
arr = [1, -2, -3, -4, 5]
s = Solution()
res = s.maxProfit(m,arr)
print(f"Maximun profit of useless laptop is {m} : {res}")

