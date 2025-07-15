
#435. Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals): 
        intervals.sort(key = lambda x:x[1] )
        n = len(intervals)
        prev = 0
        count = 1
        for i in range(1,n):
            if intervals[i][0] >= intervals[prev][1]:
                count+=1
                prev = i

        return n-count        

s = Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))

print(s.eraseOverlapIntervals([[1,2],[2,3]]))
