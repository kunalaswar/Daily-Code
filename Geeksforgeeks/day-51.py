
# Who has the majority?

class Solution:
    def majorityWins(self, arr, n, x, y):
        countx = 0
        county = 0
        for i in range(n):
            if arr[i] == x:
                countx += 1
            if arr[i] == y:
                county += 1
        
        if countx > county:
            return x
        elif county > countx:
            return y
        else:
            return min(x, y)
        
N = 11
arr = [1,1,2,2,3,3,4,4,4,4,5] # List, not set
x = 4
y = 5        
s = Solution()        
print(s.majorityWins(arr,N,x,y))

N = 8
arr= [1,2,3,4,5,6,7,8]
x = 1
y = 7
s = Solution()
print(s.majorityWins(arr,N,x,y))


