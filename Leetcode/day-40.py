
#  240. Search a 2D Matrix II
class Solution:
    def searchMatrix(self, matrix,target):
        for innermatrix in matrix:
            left = 0
            right = len(innermatrix)-1
            while(left<=right):
                    
                mid = left + (right-left)//2
                if innermatrix[mid]==target:
                    return True
                elif innermatrix[mid] < target:
                    left = mid +1
                else:
                    right  = mid -1

        return False  

s = Solution()
result = s.searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5)
print(result)

result2 = s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20)
print(result2)

