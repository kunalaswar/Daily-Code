
# 942. DI String Match
class Solution:
    def diStringMatch(self, s):
            
        low = 0
        high = len(s)
        result = []

        for char in s:
            if char == 'I':
                result.append(low)
                low += 1
            else:  # char == 'D'
                result.append(high)
                high -= 1

        # Add the last remaining number
        result.append(low)  # low == high at this point

        return result

s = Solution()
print(s.diStringMatch("IDID"))

print(s.diStringMatch("III"))
print(s.diStringMatch("DDI"))
