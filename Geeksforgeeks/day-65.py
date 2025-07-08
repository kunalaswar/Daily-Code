
# Minimum Product of k Integers

class Solution:
    def minProduct(self, arr, k): 
        lst = []
        s = 1
        for i in range(len(arr)):
            lst.append(arr[i])
            if len(lst)==k:
                # print(lst)
                s *= lst[i]
        return s  

arr = [1, 2, 3, 4, 5]
s = Solution()           
print(s.minProduct(arr, k = 2))

# arr = [9, 10, 8], k = 3