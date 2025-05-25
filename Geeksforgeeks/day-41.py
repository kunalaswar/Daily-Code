
# class Solution:
#     def common_digits(self, nums):
#         lst = []
#         for i in nums:
#                for j in str(i):
#                       if j not in lst:
#                            lst.append(j)
#                print(lst)		            
# s = Solution()                    
# s.common_digits([131, 11, 48])


class Solution:
    def common_digits(self, nums):
        lst = []
        for i in nums:
            n = i
            while(n>0):
                
                r = n%10
                if r not in lst:
                    lst.append(r)
                n = n//10
            lst.sort()    
        return lst
            
            

            
                 
s = Solution()                    
res = s.common_digits([131, 11, 48])
print(res)