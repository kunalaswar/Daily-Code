
#   Smallest number repeating K times

class Solution:
    def findDuplicate(self, arr, k):
        d = {}
        for i in arr:
          if i not in d:
            d[i]=1
          else:
            d[i]=d[i]+1
    
    
    
        sm = float("inf")
        found = False
        for val in d:
          if val<sm  and d[val]==k:
            sm = val
            found= True
        return sm if found else -1
                    
s= Solution()
arr = [2, 2, 1, 3, 1]
k = 2
print(s.findDuplicate(arr,k))

arr= [3, 5, 3, 2]
k = 1
print(s.findDuplicate(arr,k))