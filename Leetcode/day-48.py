
# 2404. Most Frequent Even Element

class Solution:
    def mostFrequentEven(self, nums):
        freq = {}
        for i in nums:
            if i%2==0:
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1
        if not freq :
            return -1 
        max_number = 0
        result = -1       

        for num in freq :
            if freq[num] > max_number or (freq[num] == max_number and num < result):
                max_number = freq[num]
                result = num

        return result 
    
s = Solution()    
print(s.mostFrequentEven([0,1,2,2,4,4,1]))

print(s.mostFrequentEven( [4,4,4,9,2,4]))
print(s.mostFrequentEven([29,47,21,41,13,37,25,7]))

