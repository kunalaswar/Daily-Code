# #  Longest Common Prefix
# def longest_common_prefix(strs):
#     if not strs:
#         return ""

#     result = ""

#     for i in range(len(strs[0])):
#         char = strs[0][i]  # take the i-th character from the first word
#         # print(char)
#         for word in strs:
#             if i >= len(word) or word[i] != char:
#                 return result  # stop when letters don't match

#         result += char  # if all matched, add the char to result

#     return result


# print(longest_common_prefix(["flower","flow","flight"]))


# def longest_common_prefix(strs):
    
#     prefix = ""

#     # zip(*strs) groups the characters from each string at the same position
#     for letters in zip(*strs):
#         # print(letters)
#         # If all characters in this position are the same
#         if len(set(letters)) == 1:
#             prefix += letters[0]  # Add it to the result
#         else:
#             break  # Stop if there's a mismatch

#     return prefix

# print(longest_common_prefix(["flower", "flow", "flight"]))

