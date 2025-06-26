
# Delete alternate characters

class Solution:
    def delAlternate(self, S):
        # Use slicing to take every character at even indices
        return S[::2]


s = Solution()
print(s.delAlternate("Geeks"))
print(s.delAlternate("GeeksforGeeks"))
