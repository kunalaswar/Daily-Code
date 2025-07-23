
# Array Leaders

class Solution:
    def leaders(self, arr):
        n = len(arr)
        lst = []
        max_from_right = arr[-1]   # Start from the rightmost element
        lst.append(max_from_right)

        for i in range(n-2, -1, -1):    # Go from second last to first
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                lst.append(arr[i])   

        lst.reverse()   # Since we added leaders from right to left, reverse the list
        print(lst)      # You can print instead of return if you're just testing




s = Solution()
# print(s.leaders([16, 17, 4, 3, 5, 2]))
s.leaders([16, 17, 4, 3, 5, 2])


        