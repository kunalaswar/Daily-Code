
# arr = [2, 3, 4, 2, 1]
# mv = max(arr)
# i = 0
# while i<=mv:
#      arr[i] = arr[i]-1
#      i = i+1
# print(arr)  


# Find unique element
class Solution:
    def find_unique(self, arr):
        count = {}
        for i  in arr:
          if i in count:
            count[i]+=1
          else:
            count[i]=1
        for j in count:
          if count[j]==1:
              return j
s = Solution()
print(s.find_unique([6, 2, 5, 2, 2, 6, 6]))
print(s.find_unique( [2, 2, 2, 10, 2]))