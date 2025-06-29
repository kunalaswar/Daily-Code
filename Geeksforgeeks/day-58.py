
# Sum Array Puzzle 

class Solution:
    def sumArray(self, arr):
        sum = 0
        for i in arr:
            sum += i

        # print(sum)    
        for i in range(len(arr)):
            arr[i] = sum-arr[i]

        return arr


s = Solution()
print(s.sumArray([3, 6, 4, 8, 9]))
print(s.sumArray([0, 0, 1]))


        

            
