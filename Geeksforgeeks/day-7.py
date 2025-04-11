
# Print 1 To N Without Loop
# Note: Don't print any newline, it will be added by the driver code.
# Doing with the help of Recursion

class Solution:    
    def printNos(self,n):
        if n==0:
            return 
        self.printNos(n-1)
        print(n,end=" " )
        

s = Solution()
res = s.printNos(5)
