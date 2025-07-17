 # 
class Solution:
    def countFreq(self, arr, target):
        freq = {}
        for i in range(len(arr)):
            if arr[i] not in freq:
                freq[arr[i]] = 1
            else:
                freq[arr[i]] += 1

        for key, value in freq.items():
            if key == target:
                return value
        return 0
s = Solution()
print(s.countFreq( [1, 1, 2, 2, 2, 2, 3], target = 2))
print(s.countFreq([1, 1, 2, 2, 2, 2, 3], target = 4))
print(s.countFreq([8, 9, 10, 12, 12, 12], target = 12))