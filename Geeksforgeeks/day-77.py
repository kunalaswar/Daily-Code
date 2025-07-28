
# Longest Common Prefix of Strings

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        if not arr:
            return ""
                
        str1 = arr[0]   
        
        for word in arr[1:]:  # Compare with rest of the strings
            while not word.startswith(str1):
                str1 = str1[:-1]  # Shorten the prefix
                if str1 == "":
                    return ""
        
        return str1
    

s = Solution()            
print(s.longestCommonPrefix( ["geeksforgeeks", "geeks", "geek", "geezer"]))
print(s.longestCommonPrefix(["hello", "world"]))
