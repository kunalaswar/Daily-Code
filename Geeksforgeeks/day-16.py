#  Print Elements of Array


class Solution:
    # Just print the space seperated array elements
	def printArray(self, arr):
	    for val in arr:
		    print(val, end = " ")
s = Solution()
s.printArray([1,2,3,4,5])