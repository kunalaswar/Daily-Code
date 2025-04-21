
# First n Fibonacci


# class Solution:
#     def fibonacciNumbers(self,n):
#         if n <=0:
#             return []
#         elif n==1:
#             return [0]
#         fib = [0,1]
#         for i in range(2,n):
#             next_num = fib[i - 1] + fib[i - 2]
#             fib.append(next_num)
#         return fib    

# s = Solution()            
# print(s.fibonacciNumbers(5))


#* fibonacci series program 

# n = int(input("Enter a number :"))
# a = 0
# b = 1
# print(a,b,end=" ")
# for i in range(n-2):
#     c = a+b
#     print(c,end=" ")    
#     a = b
#     b = c


