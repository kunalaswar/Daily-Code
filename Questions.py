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

# s = "leetcode"   
# count  = {}
# for ch in s:
#     if ch in count:
#         count[ch] += 1   
#     else:
#         count[ch] = 1

# # find first non -repeating 
# for i in range(len(s)):
#     if count[s[i]] ==1 :
#         print(i) 
#         break

# ----------------------------------------------------------
#! 4. First Non-Repeating Character
# Return the first non-repeating character in the string.
# If none exists, return None.
# Example:
# "swiss" → "w"

# s = "swiss"
# count  = {}
# for ch in s:
#     # print(ch)
#     if ch in count:
#         count[ch] +=1
#     else:
#         count[ch] = 1
# # print(count)   
# for i in range(len(s)):
#     if count[s[i]]==1:
#         print(i)
#         break

# =============================================================
#! 4. Contains Duplicate
# Return True if any value appears at least twice in the list.
# If every element is unique, return False.
# Example:
# [1,2,3,1] → True

# nums = [1,2,3,1]
# count = {}
# for i in nums:
#     if i in count:
#         count[i] +=1 
#     else:
#         count[i] = 1 
# print(count)        

# for val in count:
#     if count[val]==2:
#         print(True)
#         break
#     else:
#         print(False)    
#         break
# =============================================================

#! 5. Move Zeroes
# Given a list of integers nums, move all 0's to the end
# while maintaining the relative order of non-zero elements.
# Do not create a new list.
# Modify the list in-place.
# Example:
# [0,1,0,3,12] → [1,3,12,0,0]

nums = [0,1,0,3,12]    
pos = 0 # 1 
for i  in range(len(nums)): # [1,1,0,3,12]
    if nums[i] != 0:
        nums[pos] = nums[i]
        pos  += 1
    print(nums)
for i in range(pos,len(nums)):
    nums[i] = 0

print(nums)    

        




    

    



