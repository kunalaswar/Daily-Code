
# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lst1 = list(s)
        lst2 = list(t)

        for ch in lst2:
            if ch in lst1:
                lst1.remove(ch)
            else:
              return ch 


s = Solution()
print(s.findTheDifference(s = "abcd", t = "abcde"))

print(s.findTheDifference(s = "", t = "y"))
