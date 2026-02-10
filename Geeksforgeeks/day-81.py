
# Check if divisible by 11
class Solution:
    def divisibleBy11(self, S):
        S = str(S) 
        odd_sum = 0
        even_sum = 0

        for i in range(len(S)):
            if i % 2 == 0:      
                odd_sum += int(S[i])
            else:
                even_sum += int(S[i])

        if abs(odd_sum - even_sum) % 11 == 0:
            return 1
        else:
            return 0
s = Solution()
print(s.divisibleBy11(76945))
