
# Segregate Even and Odd numbers

class Solution:
    def segregateEvenOdd(self,arr):
        evn = []
        odd = []
        for i in range(len(arr)):
            if arr[i]%2==0:
                evn.append(arr[i])
            else:
                odd.append(arr[i])    
       
        
        if not evn :
            arr[:] = evn+odd
        if not odd:
            arr[:] = evn+odd
        else:
            evn.sort()    
            odd.sort()
            arr[:] = evn + odd
        
        return arr
     
s = Solution()
print(s.segregateEvenOdd( [12, 34, 45, 9, 8, 90, 3]))
print(s.segregateEvenOdd( [10, 22, 4, 6]))

     
