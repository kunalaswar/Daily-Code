

# 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        if n == 0 :
            return 0

        for i in range(m - n + 1):
            if haystack[i:i + n] ==needle:
                return i

        return -1  
    
s = Solution()
print(s.strStr("sadbutsad","sad"))
