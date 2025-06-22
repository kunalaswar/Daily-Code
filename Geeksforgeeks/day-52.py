 
#  Most Frequent Character


class Solution:
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self, s):
        dict = {}
        for char in s:
            if char not in dict :
                dict[char] = 1
            else:
                dict[char] += 1
        # print(dict)   
       # Step 2: Find the character with the highest frequency
        max_count = max(dict.values())
        
        # Step 3: Get all characters with max frequency
        max_chars = [char for char in dict if dict[char] == max_count]

        # Step 4: Return the lexicographically smallest one
        return min(max_chars)
      

                

s = Solution()
print(s.getMaxOccurringChar("testsample"))

print(s.getMaxOccurringChar("output"))


