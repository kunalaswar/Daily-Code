
# 852. Peak Index in a Mountain Array

class Solution:
    def peakIndexInMountainArray(self, arr):
        n = len(arr)
        left = 0
        right = n-2
        ans = n-1

        while(left<=right):
            
            mid = (left+right)//2

            if  arr[mid] < arr[mid+1]:
                # right 
                left = mid+1
            else:
                ans = mid 
                # left
                right = mid-1 
        return ans
                
s = Solution()
print(s.peakIndexInMountainArray([0,1,0]))

print(s.peakIndexInMountainArray([0,2,1,0]))

print(s.peakIndexInMountainArray([0,10,5,2]))
