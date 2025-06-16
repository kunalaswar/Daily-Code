
# 463. Island Perimeter

class Solution:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2  # subtract shared edge with top
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2  # subtract shared edge with left 
        return perimeter                 
    


s = Solution()    
print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))


print(s.islandPerimeter([[1]]))
print(s.islandPerimeter([[1,0]]))