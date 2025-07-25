
# 506. Relative Ranks

class Solution:
    def findRelativeRanks(self, score):
        # n = len(score)
        # for i in range(n):
        #     for j in range(0,n-1):
        #         if score[j]>score[j+1]:
        #             score[j],score[j+1] = score[j+1],score[j]
        # # return score
        # score = [10, 3, 8, 9, 4]
        sorted_scores = sorted(score, reverse=True)

        rank = {}
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank[s] = "Gold Medal"
            elif i == 1:
                rank[s] = "Silver Medal"
            elif i == 2:
                rank[s] = "Bronze Medal"
            else:
                rank[s] = str(i + 1)

        result = [rank[s] for s in score]
        return result
            
    
s = Solution()    
print(s.findRelativeRanks([5,4,3,2,1]))
print(s.findRelativeRanks([10,3,8,9,4]))
        
