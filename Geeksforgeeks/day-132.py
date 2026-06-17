# Minimum indexed character
# Given a string s1 and another string s2. Find the minimum index of the character in s1 that is also present in s2. if no character common in both then return -1.

# Examples :
# Input: s1 = "geeksforgeeks", s2 = "set"
# Output: 1
# Explanation: 'e' is the character which is present in given s1 "geeksforgeeks" and is also present in s2 "set". Minimum index of e is 1. 
# Input: s1 = "adcffaet", s2 = "onkl"
# Output: -1
# Explanation: There are none of the characters which is common in s1 and s2.


def minIndexChar(s1,s2): 
    for val in range(len(s1)):
        # print(val)
        if s1[val] in s2:
            return val
    return -1     
            
print(minIndexChar( "geeksforgeeks", "set"))
        
        