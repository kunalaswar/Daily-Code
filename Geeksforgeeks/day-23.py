
#Queue Using Array

class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)
    def pop(self): 
        if len(self.queue) == 0:
            return -1  
        return self.queue.pop(0) 


q= MyQueue()
q.push(10)
q.push(20)

print(q.pop())  
print(q.pop())  
print(q.pop())  


