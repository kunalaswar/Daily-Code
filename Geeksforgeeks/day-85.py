# # Non Repeating Character

# # Given a string s consisting of lowercase English Letters. return the first non-repeating character in s. If there is no non-repeating character, return '$'.

# # Examples:

# # Input: s = "geeksforgeeks"
# # Output: 'f'
# # Explanation: In the given string, 'f' is the first character in the string which does not repeat.
# # Input: s = "racecar"
# # Output: 'e'
# # Explanation: In the given string, 'e' is the only character in the string which does not repeat.
# # Input: s = "aabbccc"
# # Output: '$'
# # Explanation: All the characters in the given string are repeating.


# def nonRepeatingChar(s):
    
#     freq = {}   # dictionary to store character count
    
#     # Step 1: count frequency
#     for ch in s:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1

#     # Step 2: find first non-repeating
#     for ch in s:
#         if freq[ch] == 1:
#             return ch

#     return '$'   

# print(nonRepeatingChar("racecar"))
# print(nonRepeatingChar( "geeksforgeeks"))
# print(nonRepeatingChar("aabbccc"))

        
    
    