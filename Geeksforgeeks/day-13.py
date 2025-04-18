
# Alternates in an Array
# You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).


# class Solution:
#     def getAlternates(self, arr):
#         # Code Here
#        lst = [arr[i] for i in range(0,len(arr),2)]
#        return lst

# s = Solution()    
# print(s.getAlternates([1,2,3,4]))


#*  Using List slicing
# class Solution:
#     def getalternate(self,arr):
#         return arr[::2]
    
# s = Solution()    
# print(s. getalternate([1,2,3,4]))    

#* using for loop with index

# class Solution:
#     def getalternate(self,arr):
#         result = []
#         for i in range(len(arr)):
#             if i%2 ==0:
#                 result.append(arr[i])
#         return result

# s  = Solution()            
# print(s.getalternate([1,2,3,4]))



# class Solution:
#     def getalternative(self,arr):
#         lst = [val for idx,val in enumerate(arr) if idx %2 ==0   ]
#         return lst

# s  = Solution()            
# print(s.getalternative([1,2,3,4]))
