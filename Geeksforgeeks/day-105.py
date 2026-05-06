# Nearest multiple of 10

# A string s is given to represent a positive number. The task is to round str to the nearest multiple of 10.  If you have two multiples equally apart from s, choose the smallest element among them.

# Examples:
# Input: s = "29" 
# Output: 30
# Explanation: Close multiples are 20 and 30, and 30 is the nearest to 29. 
# Input: s = "15"
# Output: 10
# Explanation: 10 and 20 are equally distant multiples from 20. The smallest of the two is 10.


class Solution:
    def roundToNearest(self, s):

        num = int(s)

        rem = num % 10

        # if remainder less than or equal to 5
        if rem <= 5:
            return num - rem

        # otherwise round up
        else:
            return num + (10 - rem)
        
s = Solution()        
print(s.roundToNearest( "29"))



class Solution:
    def roundToNearest(self, s):

        last = int(s[-1])

        # Round Down
        if last <= 5:
            return s[:-1] + '0'

        # Round Up
        else:
            arr = list(s)

            i = len(arr) - 2

            # carry handling
            while i >= 0:

                if arr[i] != '9':
                    arr[i] = str(int(arr[i]) + 1)
                    break

                arr[i] = '0'
                i -= 1

            # if all were 9
            if i < 0:
                arr.insert(0, '1')

            arr[-1] = '0'

            return ''.join(arr)
        
        
s = Solution()        
print(s.roundToNearest( "29"))
print(s.roundToNearest( "15"))


