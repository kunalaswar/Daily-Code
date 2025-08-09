
# 
class Solution:
    def nextGreatestLetter(self, letters, target):
            
        for ch in letters:
            if ch > target: 
                return ch
        return letters[0]  

s = Solution()
print(s.nextGreatestLetter(["c","f","j"], target = "a"))
print(s.nextGreatestLetter(["c","f","j"], target = "c"))
print(s.nextGreatestLetter(["x","x","y","y"], target = "z"))