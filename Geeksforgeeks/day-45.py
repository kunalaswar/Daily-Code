
# At least two greater elements


class Solution:
    def findElements(self, arr):
        # Step 1: Sort the array in ascending order
        arr.sort()

        # Step 2: Remove the last two elements (they are the largest)
        result = arr[:-2]

        return result

    
s=Solution()
res = s.findElements([2, 8, 7, 1, 5])
print(res)
