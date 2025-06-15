

class Solution:
    def findContentChildren(self, g,s):
        g.sort()
        s.sort()
        child =  0
        cookie = 0
        while child <len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child = child+1
            
            cookie = cookie +1

        return child            

s = Solution()
res = s.findContentChildren(g = [1,2,3], s = [1,1])
print(res)