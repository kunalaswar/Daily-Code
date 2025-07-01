class Solution:
    def binarysearch(self, arr, k):
        left = 0
        right = len(arr)-1
        result = -1
        while(left<=right):
            mid = (left+right) //2
            if arr[mid]==k:
                # return mid
                result = mid  # Potential answer found
                right = mid - 1
            elif arr[mid]<k:
                left = left +1
            else:
                right  = right -1
        return result          
    

s = Solution()    
print(s.binarysearch([1, 2, 3, 4, 5], k = 4))

print( s.binarysearch([11, 22, 33, 44, 55], k = 445))

print( s.binarysearch( [1, 1, 1, 1, 2], k = 1))