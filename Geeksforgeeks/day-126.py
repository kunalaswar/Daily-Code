# String Duplicates Removal
# Given a string s which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.

# Example 1:
# Input: s = "geEksforGEeks"
# Output: "geEksforG"
# Explanation: After removing duplicate characters such as E, e, k, s, we have string as "geEksforG".
# Example 2:
# Input: s = "HaPpyNewYear"
# Output: "HaPpyNewYr"
# Explanation: After removing duplicate characters such as e, a, we have string as "HaPpyNewYr".

# 
# def removeDuplicates( s):
#     result = ""
#     for ch in s:
#         if ch not in result:
#             result += ch
#     return result

# print(removeDuplicates("geEksforGEeks"))    
# print(removeDuplicates("HaPpyNewYear"))

#	    
def removeDuplicates(s):
    set1 = set()
    result = ""       
    for i in s:
        if i not in set1:
            set1.add(i)
            result += i
    return result
    

print(removeDuplicates("geEksforGEeks"))    
print(removeDuplicates("HaPpyNewYear"))
	    



