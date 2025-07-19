
#  875. Koko Eating Bananas
# class Solution:
#     def gethours(self,piles,mid):
#         ans = 0
#         for pile in piles:
#             ans += (pile+mid-1)//mid

#         return ans 
        
#     def minEatingSpeed(self, piles,h):
#     # def minEatingSpeed(self, piles, h):
#         n = len(piles)

#         left = 1
#         right = max(piles)
#         k = right

#         while left<=right:
#             mid = (left+right)//2
#             if self.gethours(piles,mid)>h:
#                 left = mid+1
#             else:
#                 k = mid
#                 right = mid-1

#         return k     
             
        
# s = Solution()        
# print(s.gethours([3,6,7,11],  8))
# print(s.gethours([30,11,23,4,20], 5))
# print(s.gethours([30,11,23,4,20],  6))

#
class Solution:
    def gethours(self, piles, speed):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed  # Ceiling division
        return hours
        
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            if self.gethours(piles, mid) > h:
                left = mid + 1
            else:
                result = mid
                right = mid - 1

        return result



s = Solution()

# Test cases
print(s.minEatingSpeed([3,6,7,11], 8))       
print(s.minEatingSpeed([30,11,23,4,20], 5))  
print(s.minEatingSpeed([30,11,23,4,20], 6))  
