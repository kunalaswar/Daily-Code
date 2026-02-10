#
# lst = [1,2,3,4,5,6] 
# for i in lst:
#     print(i,end=" ")


# a = "2+3j"
# print(a)

# num = int(input("Enter a number :"))
# res = 'even' if num%2==0 else 'odd'
# print(res )

# num  = int(input("Enter a number :"))
# res = 'zero' if num==0  else '+ve' if num>0  else '-ve'
# print(res ) 

# a= int(input("Enter first number :"))
# b= int(input("Enter second number :"))
# res = a if a>b else b
# print(res)

# a = input("Enter a number :")
# res = 'vowel' if a in 'aeiou' else 'consonent'
# print(res)

# a = int(input("Enteer  a number :"))
# b = int(input("Enteer a  number :"))
# if a>b:
#     print(f'{a} is big  number ')
# elif b>a:
#     print(f'{b} is big  numbeer ')    
# else:
#     print("Both the value is same ")    

# word = input("Enter a word :")
# if word[::]== word[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")

# i = 1
# while(i<=10):
#     print(i)
#     i = i+1

# program for generating the  n  to 1 
# num = int(input("Enter  a number :"))
# i = num
# while(i>=1):
#     print(i)
#     i = i-1

# word= input("Enter a word :")
# i = 0
# # print(len(n))
# while(i<=len(word)-1):
#     print(word[i])
#     i = i+1 

# n  = int(input("Enter  a number :"))  
# i = 10
# while(i>=1):
#     print(n*i) 
#     i = i-1

# n = int(input("Enter a Number :"))
# i = 1
# while(i<=n):
#     print(i)
#     i = i+2

#  program for even numbre in descending order
# n = int(input("Enter number :"))
# i = n
# while(i>=0):
#     print(i)
#     i = i-2 

# for i in range(1,11):
#     print(i)

# n = 10
# for i in range(1,n+1,1):
#     print(i)

# word = input("Enter a word :")
# for i in  word:
#     print(i)

# word = input("Enter word :")
# for i in range(len(word)):
#     print(word[i])

# word = input("Enter word :")
# for i in range(-len(word),0):
#     print(word[i])

# word = input("Enter word :")
# for ch in word[::-1]:
#     print(ch)

# word = input("Enter word :")
# print(len(word)-1)
# for ch in range(len(word)-1,-1,-1):
#     print(word[ch])

# n = int(input("Enter a number :"))
# s = 0
# for i in range(1,n+1):
#     print(i)
#     s = s+i
# print("sum = ",s)    

# n =int(input("Enter a number "))
# s = 0
# ss = 0
# for i in range(n+1):
#     print(i," ",i*i)
#     s = s+i
#     ss = ss+i*i

# print(s," ",ss)        

# num = int(input("Enter a number :"))
# s = 0
# while(num>0):
#     r = num%10  
#     s = s+r
#     num = num//10
# print(s)    

# num = int(input("Enter a number :"))
# lst = []
# while(num>0): 
#     d = num%10
#     if d%2==0:
#         lst.append(d)
#         num = num//10

# print(lst.reverse())

# program for demorastring the break statement 
# s = 'python'
# for ch in s:
#     if ch =='o':
#      break
#     print(ch,end="")

# s = "python"
# i = 0
# while(i<len(s)):
#     if s[i]=="o":
#         break
#     print(s[i])
#     i = i+1


# s = "MISSISIPI"
# count = 0
# for i in s:
#     if i=="I":
#         count = count +1
#     if count==2:
#         break
#     print(i)    

# print(count)

# s = "MISSISIPI"
# count = 0
# i = 0
# while(len(s)>i):
#     if s[i]=="I":
#         count = count+1
#     if count ==2:
#         break
#     print(s[i])     
#     i = i+1
# print(count)    

# s = 'python'
# for i in s:
#     if i == 't':
#         continue
#     print(i)

# s = "python"
# i = 0
# while(i<len(s)):
#     if s[i]=='t':
#         i = i+1
#         continue
#     print(s[i])
#     i = i+1


# n = int(input("Enter a number : "))
# if n<=1:
#     print("invalid input ")
# else:
#     res = 'prime'   
#     for i in range(2,n):
#         if n%i==0:
#             res = 'not prime'
#             break
# print(res)        

# n = int(input("Enter :"))
# i = 2
# if n<=1:
#     print("invalid input ")
# else:
#     res = 'prime'    
#     while(i<n):
#         if n%i==0:
#             res= 'not prime'
#             break
#         i = i+1
# print(res)        

# line = input("enter a text :")
# x = line.split()
# # print(x)
# for i in x:
#     if len(i)==2 or len(i)==3:
#         print(i)

# n = int(input("Enter a number :"))
# for i in range(2,n+1):
#     res = "Prime"
#     for j in range(2,i):
#         if i%j==0:
#             res ='not prime'
#             break
#     if res =="Prime"  :
#         print(i)

# def reverseword(s):
#     x = s.split()
#     lst = []
#     for i in x:
#         lst.append(i[::-1])
        
#     s = " ".join(lst)  
#     return s
# n = input("Enter : ")      
# a = reverseword(n)
# print(a)
  

# lst = [10,20,30,40,-50,-70]
# pl = [val for val in lst  if val>0]
# nl = [val for val in lst if val<0]
# print(pl)
# print(nl)

# nlst = [float(val) for val in input("Enter a value ").split() if float(val)<0]
# print(nlst)
# pslt = [float(val) for val in  input ("Enter  value :").split() if float(val)>0]
# print(pslt)

# def decideprime(val):
#     res = 1
#     for i in range(2,val):
#         if val%i==0:
#             res = 0
#             break
#     return res     

# # decideprime()
# vals = [int(val) for val in input().split() if int(val)>1]
# print(vals)
# prime = [int(val) for val in vals if decideprime(val) ]
# print(prime)

# def addop(a,b):
#     return(a+b)

# res = addop(2,3)
# print(res)

# n = input("Enter :")
# lst = [int(val) for val in n ]
# poslist = list(filter(lambda val :val>0,lst))
# neglist = list(filter(lambda val :val<0,lst))
# print(poslist)
# print(neglist)

# word = input("Enter a  list of value :")
# lst = [i.lower() for i in word]
# vwords = list(filter(lambda word : 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word,lst ))
# print(vwords)

# def ranges(x):
#     s = 0
#     while(s<x):
#         yield s
#         s = s+1

# r = ranges(5)
# # print(r)
# for val in r:
#     print(val)


# def getcr():
#     yield "python"
#     yield "HTML"
#     yield "Django"
#     yield "c"
#     yield '1.2'
#     yield 1.2

# gs = getcr()    
# print(gs)
# for val in gs:
#     print(val)



