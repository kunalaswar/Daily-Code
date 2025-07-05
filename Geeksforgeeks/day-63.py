

class Solution:
    def mostFreqEle(self, arr):
        # code here
        dict1 = {}
        for  i in arr:
            if i in dict1:
                dict1[i] +=  1
            else:
                dict1[i] = 1
        # print(dict1)      
        max_freq = 0
        result = float('-inf')  # So even negative numbers can be chosen

        for num in dict1:
            if dict1[num] > max_freq or (dict1[num] == max_freq and num > result):
                max_freq = dict1[num]
                result = num

        return result
s  = Solution()        
print(s.mostFreqEle([1, 2, 2, 2, 4, 1]))

print(s.mostFreqEle([1, -5, 8, 1]))

print(s.mostFreqEle( [3, 0, 0, 3, 8]))