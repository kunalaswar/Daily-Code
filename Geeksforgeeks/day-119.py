# Find all pairs with a given sum
#User function Template for python3

# class Solution:
#     def allPairs(self, target, arr1, arr2):
#         for i in range(len(arr1)):
#             for j in range(len(arr2)-1):
#                 if arr1[i]+arr2[j]==target:
                    # return arr1[i] ,arr2[j]
class Solution:
    def allPairs(self, target, arr1, arr2):
        lst = []
        arr1.sort()
        for i in arr1:
            for j in arr2:
                if i+j==target:
                    lst.append((i,j))
        return lst            

s = Solution()
print(s.allPairs(9 ,[1, 2, 4, 5, 7],[5, 6, 3, 4, 8]))

class Solution:
    def allPairs(self, target, arr1, arr2):
        lst = []
        freq = {}
        # count frequencies
        for num in arr2:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        arr1.sort()
        for i in arr1:
            value = target - i
            if value in freq:
                for j in range(freq[value]):
                    lst.append((i, value))
        return lst

s = Solution()
print(s.allPairs(9 ,[1, 2, 4, 5, 7],[5, 6, 3, 4, 8]))
print(s.allPairs( 8, [-1, -2, 4, -6, 5, 7], [6, 3, 4, 0]))
print(s.allPairs( 9, [1, 2, 4, 5, 7, 4],[5, 6, 3, 4, 8, 4]))

