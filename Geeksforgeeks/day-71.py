
#  Frequencies in a Limited Array
class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        freq = [0] * n  # Initialize result array of size n with 0s
        # print(freq)
        for num in arr:
            if 1 <= num <= n:   # Only count numbers within 1 to n
                freq[num - 1] += 1

        return freq
        
s = Solution()
print(s.frequencyCount([2, 3, 2, 3, 5]))  #output :  [0, 2, 2, 0, 1]
print(s.frequencyCount([3, 3, 3, 3]))
print(s.frequencyCount([1]))
