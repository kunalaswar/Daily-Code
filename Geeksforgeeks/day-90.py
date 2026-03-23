# Anagram

# Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
# Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.

# Examples:
# Input: s1 = "geeks" s2 = "kseeg"
# Output: true 
# Explanation: Both the string have same characters with same frequency. So, they are anagrams.
# Input: s1 = "allergy", s2 = "allergyy" 
# Output: false 
# Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams. 
# Input: s1 = "listen", s2 = "lists" 
# Output: false 
# Explanation: The characters in the two strings are not the same — some are missing or extra. So, they are not anagrams.

class Solution:
    def areAnagrams(self, s1, s2):
       dict1 ={}
       dict2 = {}
       if len(s1)!=len(s2):
           return False
       for i in s1:
           if i not in dict1:
               dict1[i] = 1
           else:
               dict1[i] += 1                   
       for i in s2:           
           if i not in dict2:
                dict2[i] = 1
           else:
               dict2[i] += 1 

       return dict1 == dict2
                 
s = Solution()       
print(s.areAnagrams("geeks","kseeg"))
print(s.areAnagrams("allergy", "allergyy"))
print(s.areAnagrams("listen","lists" ))

#! OR

class Solution:
    def areAnagrams(self,s1, s2):

        if len(s1) != len(s2):
            return False

        freq = {}

       
        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1

        # subtract from s2
        for ch in s2:
            if ch not in freq:
                return False
            freq[ch] -= 1

        
        for val in freq:
            if freq[val] != 0:
                return False

        return True


s = Solution()       
print(s.areAnagrams("geeks","kseeg"))
print(s.areAnagrams("allergy", "allergyy"))
print(s.areAnagrams("listen","lists" ))


