
# #   Implement stack using array

class MyStack:
    def __init__(self):
        self.arr=[]
    
    def push(self,data):
        self.arr.append(data)
        
    def pop(self):
        if len(self.arr) == 0:
            return -1
        return self.arr.pop()
    

query = '1,2,1,3,2,1,4,2'  
tokens = list(map(int,query.split(',')))

stack = MyStack()
output = []

i = 0
while i < len(tokens):
    if tokens[i]==1:
        stack.push(tokens[i+1])
        i = i+2
    elif tokens[i]==2:
        output.append(stack.pop())    
        i = i+1

print(",".join(map(str,output)))



# num= 123,56
# sum of digits = 6


