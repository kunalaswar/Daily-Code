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

nums = [0, 1, 0, 3, 12]
# pos = 0 # 1
# for i  in range(len(nums)): # [1,1,0,3,12]
#     if nums[i] != 0:
#         nums[pos] = nums[i]
#         pos  += 1
#     print(nums)
# for i in range(pos,len(nums)):
#     nums[i] = 0
# print(nums)

#! method 2
# temp = []
# for i in range(0,len(nums)):
#     if nums[i]!=0:
#         temp.append(nums[i])
# # nz= len(temp)
# for i in range(0,len(temp)):
#     nums[i] = temp[i]

# for i in range(len(temp),len(nums)):
#     nums[i]=0

# print(nums)

#! method 3
# nums = [0,1,0,3,12]
# i =0
# while(i<len(nums)):
#     if nums[i]==0:
#         break
#     i = i+1
# if i==len(nums):
#     pass # return
# j = i+1
# while(j<len(nums)):
#     if nums[j]!=0:
#         nums[i],nums[j] = nums[j],nums[i]
#         i = i+1
#     j = j+1
# print(nums)


#! 4. Valid Anagram
# Return True if one string is an anagram of another.
# Example:
# "anagram", "nagaram" → True

# s = "anagram"
# t = "nagaram"
# count1 = {}
# count2 = {}
# for i in range(len(s)):
#     if s[i] not in count1:
#         count1[s[i]] = 1
#     else:
#         count1[s[i]] += 1
# print(count1)
# for i in range(len(t)):
#     if t[i] not in count2:
#         count2[t[i]] = 1
#     else:
#         count2[t[i]] += 1
# print(count2)

# if count1 != count2: # Order does NOT matter in dictionary comparison.
#     print(False)

# else:
#     print(True)

#! method 2
# s = "anagram"
# t = "nagaram"
# count1 = {}
# count2 = {}
# if len(s)!=len(t):
#     print(False)

# else:
#     count = {}

#     for ch in s:
#         count[ch] = count.get(ch,0) + 1

# # print(count)
#     for ch in t:
#         if ch not in count:
#             print(False)
#             break
#         count[ch] -=1
#         if count[ch] < 0:
#             print(False)
#             break

#     else:
#         print(True)

# ===============================================================
#! 5. Longest Common Prefix
# Find the longest common prefix among an array of strings.
# Example:
# ["flower","flow","flight"] → "fl"

# def longest_common_prefix(strs):
#     if not strs:
#         return ""

#     prefix = ""
#     for i in range(len(strs[0])):
#         char = strs[0][i]
#         for word in strs[1:]:
#             if i >= len(word) or word[i] != char:
#                 return prefix
#         prefix += char
#     return prefix

# print(longest_common_prefix(["flower", "flow", "flight"]))

# strs = ["flower","flow","flight"]
# prefix = strs[0]
# # print(prefix)
# for s in strs[1:]:
#     # print(s)
#     while not s.startswith(prefix):
#         prefix = prefix[:-1] # reduce the lenght
#         if not prefix:
#             break
# print(prefix)


# ===============================================================
#! 6. Best time to buy and sell the stock
# Return maximun profit from one buy and one sell

# lst = [7,1,5,3,6,4]
# min_price = lst[0]
# max_profit = 0

# for i in lst:
#     if i < min_price:
#         min_price = i # 1
# # # print(min_price)
#     profit = i-min_price
#     # print(profit)
#     if profit > max_profit:
#         max_profit = profit

# print("profit : ",max_profit)


# ===============================================================
#! 7. merge sorted array
#  Marge two sorted arrays into one sorted array in place

# a = [1,2,3,0,0,0]
# b = [2,5,6]

# m = 3
# n = 3
# i = m-1
# j = n-1
# k = m + n - 1
# while(i>=0 and j>=0):
#     if a[i]>b[j]:
#         a[k] = a[i]
#         i = i-1
#     else:
#         a[k]=b[j]
#         j = j-1
#     k = k - 1

# while(j>=0):
#     a[k] = b[j]
#     j = j-1
#     k = k-1
# print(a)


# ===============================================================
#! 8. majority element
# find the element that appear more than n/2 times

# lst = [3,2,3]
# count = {}
# for i in lst:
#     if i not in count:
#         count[i] = 1
#     else:
#         count[i] += 1
# # print(count)
# for val in count:
#     if count[val] > 3:
#         print(val)


# boyers more voting
# lst = [3,2,3]
# candidate = None
# count = 0
# for num in lst:
#     if count ==0:
#         candidate = num
#     count +=1 if num == candidate  else -1
# print(candidate)

# ===============================================================
#! 9. Intersection of two Array
# Return the intersection of two arrays continue elements
# Eaxmples

# lst1 = [1,2,2,1]
# lst2 = [2,2]
# common_element = set()
# for i in lst1:
#     if i in lst2:
#         common_element.add(i)
# print(common_element)

#
# lst1 = [1,2,2,1]
# lst2 = [2,2]
# set2 = set(lst2)
# common_element = set()
# for i in lst1:
#     if i in set2:
#         common_element.add(i)
# print(common_element)


# ===============================================================
#! 10.Top k Frequent Elements
# Return  the k most frequent elements
# Example :

# nums = [1,1,1,2,2,3]
# k = 2
# dict1 = {}
# for i in nums:
#     if i not in dict1:
#         dict1[i] = 1
#     else:
#         dict1[i] += 1
# # print(dict1)
# sorted_item = sorted(dict1.items(),  key=lambda x : x[1], reverse = True)

# result = [key for key in sorted_item[:k]]
# print(result)

# ===============================================================
# stack
#! 11. valid paranthesis
# check if paranthesis are valid
# Example :
# "(),[],{}" = True

# def isvalid(s):

#     stack = []
#     pairs = {')':'(', ']':'[', '}':'{'}
#     for ch in s:
#         if ch in pairs.values():
#             stack.append(ch)
#         else:
#             if not stack:
#                 return  False
#             if stack[-1] !=pairs[ch]:
#                 return False
#             stack.pop()
#     return len(stack)== 0
# print(isvalid("()[]{}"))

#
# def isvalid(s):
#     stack = []
#     closetoopen = {')':'(', ']':'[', '}':'{'}
#     for ch in s:
#         if ch in closetoopen:
#             if not stack or stack[-1] != closetoopen[ch]:
#                 return False
#             stack.pop()
#         else:
#             stack.append(ch)
#     return not stack

# print(isvalid("()[]{}"))
# print(isvalid("(["))


# ===============================================================
#! 12. min stack
# Design the stack that support retriving the minimun element in po(1)

# class Minstack:
#     def __init__(self):
#         self.stack = []

#     def push(self,val):
#         if not self.stack:
#             self.stack.append((val,val))
#         else:
#             current_min  = min(val,self.stack[-1][1])
#             self.stack.append((val,current_min))

#     def pop(self):
#         self.stack.pop()

#     def top(self):
#         return self.stack[-1][0]

#     def getmin(self):
#         return self.stack[-1][1]

# s = Minstack()
# s.push(5)
# s.push(3)
# s.push(7)
# print(s.stack)
# print(s.top())
# print(s.getmin())

# s.pop()
# print(s.getmin())

# s.pop()
# print(s.getmin())


# ===============================================================
#! 13. Factorial
# compute factorial using Recursion & normal

# normal factorial
# n = int(input("Enter a value : "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

# Recursion
# def fact(n):
#     if n == 0:
#          return 1
#     else:
#         return n * fact(n-1)

# n = int(input("Enter value : "))
# print(fact(n))


# ===============================================================
#! 14. Fibonacci number
# return the n fibonacci number

# n = int(input("Enter  a value : "))
# a = 0
# b = 1
# for i in range(n):
#     temp = a+b
#     a = b
#     b = temp
# print(a)


# ===============================================================
#! 15. Two pointers
# Remove duplicates from sorted array

# nums = [0,0,1,1,2,2,3,3,4]

# i = 0

# for j in range(1,len(nums)):
#     if nums[j]!=nums[i]:
#         i+=1
#         nums[i] = nums[j]
# print(i+1)
# print(nums[:i+1])

# ===============================================================
#! 16. squares of a sorted array
# Return the sorted array of squares

# lst = [-4,-1,0,3,10]

# for i in range(len(lst)):
#     lst[i] = lst[i]*lst[i]

# lst.sort()
# print(lst)

#
# lst = [-4,-1,0,3,10]
# n = len(nums)
# ans = [0]*n

# i = 0
# j = n-1
# k = n-1
# while(i<=j):
#     if abs(nums[i])>abs(nums[i]):
#         ans[k] = nums[i]* nums[i]
#         i = i+1
#     else:
#         ans[k] = nums[j]* nums[j]
#         j = j-1
#     k = k-1

# print(ans)


#
# def sortedsquares(nums):
#     left , right = 0, len(nums)-1
#     res = []

#     while left <= right :
#         if nums[left] * nums[left] > nums[right]*nums[right]:
#             res.append(nums[left]*nums[left])
#             left += 1
#         else:
#             res.append(nums[right]*nums[right])
#             right -=1
#     return res[::-1]
# print(sortedsquares([-4,-1,0,3,10]))


# ===============================================================
#! 17.  subarray num Equals k
# count subarray whose sum equals to k brute force approach

# def subarray(nums,k):
#     sums = 0
#     lst = []
#     for i in nums:
#         lst.append(i)
#         nums += lst

# nums = [1,1,1]
# k = 2
# print(subarray(nums,k))


# nums = [1, 1, 1]
# k = 2
# count = 0

# for i in range(len(nums)):
#     # print(nums[i])   
#     sum = 0   
#     for j in range(i,len(nums)):
#         print(j)
#         sum +=nums[j]
#         print("-------")
#         if sum == k:
#             count += 1
# print(count,"===")            

# ===============================================================
#! 18.  Group Anagram
# Group string that are anagrams 

# Anagram : Two strings are anagram if
#           they contain the same letter 
#           with same frequency
#           but the order can be different 

# eat , ate , tea -> anagram 

# from collections import defaultdict 
# class Solution:
#     def groupAnagram(self,strs):
#         groups = defaultdict(list)

#         for s in strs :
#             key = ''.join(sorted(s))
#             groups[key].append(s)
#         return list(groups.values())    

# s = Solution()    
# print(s.groupAnagram(["eat","tea","tan","ate","nat","bat"]))


# ===============================================================
#! 19.product of array except self
# Return array where each element is product of all other 
# nums = [1,2,3,4]
# op = [24,12,8,6]

# nums = [1,2,3,4]
# n = len(nums)
# ans = [1]*n
# prefix = 1 
# for i in range(n):
#     ans[i] =prefix 
#     prefix *=nums[i]

# suffix = 1 
# for i in range(len(nums)-1,-1,-1):
#     ans[i] *= suffix
#     suffix *= nums[i]

# print(ans)
#
# nums = [1,2,3,4]
# lst  = [] 

# for i in range(len(nums)):
#     product = 1         
#     # print(i)
#     for j in range(len(nums)):
#         if i!=j:   
#             product *= nums[j]
#             # print(product)
#             # print("------")
#     lst.append(product)    
# print(lst)
        

# ===============================================================
#! 20.Count the Zeros

#Given an array arr of only 0's and 1's. The array is sorted in such a manner that all the 1's are placed first and then they are followed by all the 0's. Find the count of all the 0's.

# Input: arr[] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
# Output: 3
# Explanation: There are 3 0's in the given array.
# Input: arr[] = [0, 0, 0, 0, 0]
# Output: 5
# Explanation: There are 5 0's in the array.

def countZeroes(arr):
    count = 0
    for num in arr:
        if num==0:
            count = count + 1 
    print(count)        



countZeroes([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0])
countZeroes([0, 0, 0, 0, 0])

