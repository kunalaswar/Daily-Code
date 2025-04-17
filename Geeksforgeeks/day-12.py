
class Solution:
    def rotate(self, arr):
        if not arr:
            return arr
        else:
                
            last_ele = arr[-1]   
            arr.pop()
            arr.insert(0,last_ele)
            return arr
            
arr = [1,2,3,4,5]
s = Solution()
print(s.rotate(arr))

