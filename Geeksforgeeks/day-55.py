

#   Palindrome Array


class Solution:
    def isPerfect(self, arr ):
        # code here
        left = 0
        right = len(arr) -1 
        while(left < right):
            
            if arr[left]!=arr[right]:
                return False        
            
            else:
                
                left += 1
                right -=1
        return True
                
s = Solution()                
print(s.isPerfect([1, 2, 3, 2, 1]))

print(s.isPerfect( [1, 2, 3, 4, 5]))
                
            