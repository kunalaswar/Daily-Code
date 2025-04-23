# Your task is to complete this function
# Function should return true/false
# def isPalinArray(arr):
   
#     for num in arr:
#         if str(num) != str(num)[::-1]:
#             return False
            
#     return True

# arr = [int(val) for val in input().split()]
# s = isPalinArray(arr)
# print(s)        
    
    
#* OR 

# def is_palindrome(arr):
#     if len(arr)==0:
#         return []
#     else:
#         for val in arr:

#             original =val
#             reverse = 0
#             while(val>0):
#                 digit  = val % 10
#                 reverse = reverse * 10 +digit
#                 val = val //10
#             if reverse != original:
#                 return False
#     return True
# arr = [int(val) for val in input().split()]        
# s = is_palindrome(arr)        
# print(s)




