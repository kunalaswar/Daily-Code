
#   Data Type

class Solution:
    def dataTypeSize(self, str):
        if str == "Character":
            return 1
        elif str == "Integer":
            return 4
        elif str == "Long":
            return 8
        elif str == "Float":
            return 4
        elif str == "Double":
            return 8
        else:
            return -1
 
sol = Solution()
print(sol.dataTypeSize("Character"))  # Output: 1
print(sol.dataTypeSize("Integer"))    # Output: 4
print(sol.dataTypeSize("Boolean"))    # Output: -1 
