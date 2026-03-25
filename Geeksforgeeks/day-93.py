# Moves zeros 
# moves all the zero while maintaining order 

# lst = [0,1,0,3,12]
# lst2 = []
# count = 0
# for i in lst:
#     if i != 0 :
#         lst2.append(i)
#     # print(lst2)        
#     else:
#         count = count + 1 
# # print(count)
# for i in range(count):
#     lst2.append(0)
# print(lst2)    

# or 

lst = [0,1,0,3,12]
pos = 0
for i in range(len(lst)):
    if lst[i] !=  0:
        lst[pos] = lst[i]
        pos +=1
 
for i in range(pos,len(lst)):
    lst[i] = 0

print(lst)








