
# 74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix,target):
        for innermatrix in matrix:
                
            left = 0
            right = len(innermatrix) -1
            while(left<=right):
                mid = left + (right-left)//2
                if innermatrix[mid]==target:
                    return True
                elif innermatrix[mid] < target:
                    left = mid +1
                else:
                    right  = mid -1

        return False 
    

s  = Solution()    
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
