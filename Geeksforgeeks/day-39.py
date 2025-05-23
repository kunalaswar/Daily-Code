

def lastIndex(s):

    for i in range(len(s)-1,-1,-1):
        if s[i]=='1':
            return i
    else:
        return -1

s = '00001'
print(lastIndex(s))    
s = '0'
print(lastIndex(s))    


                
                