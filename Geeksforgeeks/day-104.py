# Alternate Positive Negative

# Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.

# Note:
# - Resulting array should start with a positive integer (0 will also be considered as a positive integer).
# - If any of the positive or negative integers are exhausted, then add the remaining integers in the answer as it is by maintaining the relative order.
# - The array may or may not have the equal number of positive and negative integers.

# Examples:
# Input: arr[] = [9, 4, -2, -1, 5, 0, -5, -3, 2]
# Output: [9, -2, 4, -1, 5, -5, 0, -3, 2]
# Explanation: The positive numbers are [9, 4, 5, 0, 2] and the negative integers are [-2, -1, -5, -3]. Since, we need to start with the positive integer first and then negative integer and so on (by maintaining the relative order as well), hence we will take 9 from the positive set of elements and then -2 after that 4 and then -1 and so on.

# Input: arr[] = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
# Output: [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]
# Explanation : The positive numbers are [5, 2, 4, 7, 1, 8, 0] and the negative integers are [-5,-2,-8]. According to the given conditions we will start from the positive integer 5 and then -5 and so on. After reaching -8 there are no negative elements left, so according to the given rule, we will add the remaining elements (in this case positive elements are remaining) as it in by maintaining the relative order.
# Input: arr[] = [9, 5, -2, -1, 5, 0, -5, -3, 2]
# Output: [9, -2, 5, -1, 5, -5, 0, -3, 2]

# Explanation: The positive numbers are [9, 5, 5, 0, 2] and the negative integers are [-2, -1, -5, -3]. Since, we need to start with the positive integer first and then negative integer and so on (by maintaining the relative order as well), hence we will take 9 from the positive set of elements and then -2 after that 5 and then -1 and so on.

class Solution:
    def rearrange(self, arr):
        pos = []
        neg = []

        # Step 1: separate
        for num in arr:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        i = 0
        j = 0
        k = 0

        # Step 2: alternate
        while i < len(pos) and j < len(neg):
            arr[k] = pos[i]
            k += 1
            i += 1

            arr[k] = neg[j]
            k += 1
            j += 1

        # Step 3: remaining
        while i < len(pos):
            arr[k] = pos[i]
            k += 1
            i += 1

        while j < len(neg):
            arr[k] = neg[j]
            k += 1
            j += 1
        print(arr)            

s = Solution()
s.rearrange([9, 4, -2, -1, 5, 0, -5, -3, 2])
        
