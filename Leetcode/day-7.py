# 58. Length of Last Word


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s
        word_list = s.split()
        last_word = word_list[-1]
        count = 0
        for val in last_word:
            count = count+1
        return count
    
s = Solution()
res = s.lengthOfLastWord("Hello World")
print(res)