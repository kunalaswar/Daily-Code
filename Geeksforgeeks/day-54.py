
#Remove vowels from string

class Solution:
    def removeVowels(self, s):
        vowels = "aeiouAEIOU"
        result = ""
        for char in s:
            if char not in vowels:
                result += char
        return result


s = Solution()
print(s.removeVowels("welcome to geeksforgeeks"))       
print(s.removeVowels("what is your name ?"))            

