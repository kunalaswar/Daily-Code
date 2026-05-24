# Intersection of two sorted arrays
# Given two sorted arrays arr1[] and arr2[]. Your task is to return the intersection of both arrays.
# Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not count duplicate elements.
# Note: If there is no intersection then return an empty array.

# Examples:
# Input: arr1[] = [1, 2, 3, 4], arr2[] = [2, 4, 6, 7, 8]
# Output: [2, 4]
# Explanation: 2 and 4 are only common elements in both the arrays.
# Input: arr1[] = [1, 2, 2, 3, 4], arr2[] = [2, 2, 4, 6, 7, 8]
# Output: [2, 4]
# Explanation: 2 and 4 are the only common elements.
# Input: arr1[] = [1, 2], arr2[] = [3, 4]
# Output: []
# Explanation: No common elements.

# class Solution:
#     def intersection(self, arr1, arr2):
#         # print(arr1,arr2)
#         set1  = set()
#         for i in arr1:
#             if i in arr2:
#                 set1.add(i)
#         return sorted(list(set1))
        

# s = Solution()
# print(s.intersection(arr1 = [1, 2, 3, 4], arr2 = [2, 4, 6, 7, 8]))
# print(s.intersection([1, 2, 2, 3, 4], [2, 2, 4, 6, 7, 8]))
# print(s.intersection([1, 2], [3, 4]))        
    
# 
class Solution:
    def intersection(self, arr1, arr2):
        s = set(arr2)
        seen = set()
        ans = []
        for i in arr1:
            if i in s and i not in seen:
                ans.append(i)
                seen.add(i)
        return ans


s = Solution()
print(s.intersection(arr1 = [1, 2, 3, 4], arr2 = [2, 4, 6, 7, 8]))
print(s.intersection([1, 2, 2, 3, 4], [2, 2, 4, 6, 7, 8]))
print(s.intersection([1, 2], [3, 4]))        
    
