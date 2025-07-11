# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in s :
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] +=1
        
        for index,char in enumerate(s):
            if freq[char] == 1:
                return index

        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar( "loveleetcode"))
print(s.firstUniqChar("aabb"))
