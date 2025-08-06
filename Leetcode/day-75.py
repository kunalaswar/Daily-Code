class Solution:
        
    def floodFill(self,image, sr, sc, color):
        old_color = image[sr][sc]
        
        # If the color is already the same, do nothing
        if old_color == color:
            return image

        def dfs(r, c):
            # If out of bounds or color is not same as old, return
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            if image[r][c] != old_color:
                return

            # Change the color
            image[r][c] = color

            # Move in 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        dfs(sr, sc)
        return image
s  = Solution()
print(s.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))

print(s.floodFill( image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0))