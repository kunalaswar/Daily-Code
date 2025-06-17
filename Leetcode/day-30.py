 
# 1431. Kids With the Greatest Number of Candies

# class Solution:
#     def kidsWithCandies(self, candies, extraCandies):
#         maxcandies = max(candies)
#         lst = []
#         for i in candies:
#             if (i + extraCandies) >= maxcandies:
#                 lst.append(True)
#             else:
#                 lst.append(False)    
#         return lst   

        
# s = Solution()        
# res = s.kidsWithCandies([2,3,5,1,3],3)
# print(res)

# s = Solution()        
# res1 = s.kidsWithCandies([4,2,1,1,2],1)
# print(res1)
# s = Solution()        
# res2 = s.kidsWithCandies([12,1,12], 10)
# print(res2)


# OR  Using list compersion 

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxcandies = max(candies)

        lst = [ (i+extraCandies) >= max(candies)  for i in candies ]
        return lst

s = Solution()        
res = s.kidsWithCandies([2,3,5,1,3],3)
print(res)




