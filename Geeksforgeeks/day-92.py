# contains dublicate
# return true if any appears atleast twice 

 # Ex : [1,2,3,1] -> True

# lst = [1,2,3,1]
# count  = {}
# for i  in lst:
#     if i not in count:
#         count[i] = 1
#     else:
#         count[i] +=1
# # print(count)        
# for val in count:
#     if count[val]>=2:
#         print(True)
#         break
# else:
#     print(False)    

# or 
# lst = [1,2,3,4,1]
# print(len(lst)!=len(set(lst)))

lst = [1,2,3,1]
seen  =set()
for i in lst:
    if i in seen:
        print(True)
        break
    seen.add(i)
else:
    print(False)    
    
      




    

