
# Remove Duplicates from unsorted array

class Solution:
    def removeDuplicate(self, arr):
      
        set1 = set()
        lst = []
        for num in arr:
            if num not in set1:
                set1.add(num)
                lst.append(num)
        return lst
    
s = Solution()    
print(s.removeDuplicate([1, 2, 3, 1, 4, 2]))
print(s.removeDuplicate([1, 2, 3, 4]))
