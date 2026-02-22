#! 1. Reverse String
# Given a list of characters s, reverse it in-place.
# Do not create a new list.
# Do not use slicing (s[::-1]).
# Example:
# ["h","e","l","l","o"] → ["o","l","l","e","h"]

# s = ["h","e","l","l","o"]
# # print(s[::-1])

# left = 0 
# right = len(s)-1
# while(left < right):
#     s[left],s[right] = s[right] ,s[left ]
#     left += 1 
#     right -= 1
# print(s)

# -----------------------------------------------------------
#! 2. Valid Palindrome
# Return True if a string is a palindrome,
# considering only alphanumeric characters and ignoring case.
# Do not use slicing (s[::-1]).
# Example:
# "A man, a plan, a canal: Panama" → True

# s = "A man, a plan, a canal: Panama"
# left = 0
# right = len(s)-1
# # print(left , right)
# while(left<right):
#     # "Keep skipping until character becomes valid." that why we use the while 
#     while left <right and not s[left].isalnum(): # amanaplanacanalpanama
#         left += 1
#     while left < right and not s[right].isalnum():
#         right -= 1 
#     if s[left].lower() !=  s[right].lower():
#         print(False)
#         break 

#     left += 1 
#     right -= 1 
# else:
#     print(True)

# ------------------------------------------------

#! 3. First Unique Character in a String
# Return the index of the first non-repeating character.
# If none exists, return -1.
# Example:
# "leetcode" → 0

s = "leetcode"   

count  = {}
for ch in s:
    if ch in count:
        count[ch] += 1   
    else:
        count[ch] = 1

# find first non -repeating 
for i in range(len(s)):
    if count[s[i]] ==1 :
        print(i) 
        break





# def first_unique_char(s):

#     # Step 1: Count frequency
#     count = {}

#     for ch in s:
#         count[ch] = count.get(ch, 0) + 1

#     # Step 2: Find first non-repeating
#     for i in range(len(s)):
#         if count[s[i]] == 1:
#             return i

#     return -1

    








    

    



