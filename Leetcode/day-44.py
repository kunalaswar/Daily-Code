
#  
class solution:
        
    def find_error_nums(self,nums):
        n = len(nums)
        duplicate = -1
        missing = -1

        # Step 1: Create a count array to track occurrences
        count = [0] * (n + 1)  # index from 1 to n

        for i in range(n):
            count[nums[i]] += 1

        # Step 2: Identify duplicate and missing
        for i in range(1, n + 1):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                missing = i

        return [duplicate, missing]
# Usage
s = solution()
print(s.find_error_nums([1, 2, 2, 4]))  # Output: [2, 3]

print(s.find_error_nums([1,1]))
