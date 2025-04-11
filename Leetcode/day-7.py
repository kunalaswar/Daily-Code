# 58. Length of Last Word


# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s
#         word_list = s.split()
#         last_word = word_list[-1]
#         count = 0
#         for val in last_word:
#             count = count+1
#         return count
    
# s = Solution()
# res = s.lengthOfLastWord("Hello World")
# print(res)


# import typing import List 
# def length_of_last_word(s: str) -> int:
#     s = s.strip()            # Remove any trailing or leading spaces
#     words = s.split()        # Split the string into a list of words
#     return len(words[-1])    # Return the length of the last word

# s = "Hello World"
# print(length_of_last_word(s))

