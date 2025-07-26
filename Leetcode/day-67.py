
# 566. Reshape the Matrix

class Solution:
    def matrixReshape(self, mat,r,c):
        total = len(mat) * len(mat[0])
        if total != r * c:
            return mat
        
        
        flat = []
        for row in mat:
            for val in row:
                flat.append(val)
        
        
        reshaped_list = []
        for i in range(r):
            reshaped_list.append(flat[i * c : (i + 1) * c])
        
        return reshaped_list

s = Solution()
print(s.matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))

print(s.matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4))
