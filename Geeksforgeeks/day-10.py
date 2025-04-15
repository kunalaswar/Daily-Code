 
#Count Odd and Even


class Solution:
    def countOddEven(self,arr):
        ecount = 0
        ocount = 0
        for val in arr:
            if val %2 ==0:
                ecount = ecount +1
            else :
                ocount = ocount +1
        return ocount ,ecount      
     
s = Solution()   
res = s.countOddEven([1,2,3,4,5,6])       
print(res)     
     
