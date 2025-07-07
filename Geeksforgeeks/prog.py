
# Sort The Array
# arr = [1, 5, 3, 2]
# for i in range(len(arr)):
#  for  j in range(i+1,len(arr)):
#      if arr[i]>arr[j]:
#           arr[i],arr[j] = arr[j],arr[i]
# print(arr)






# Count Linked List Nodes
# Given a singly linked list. The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.

'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        count = 0
        current = head
        while current:
            count = count+1
            current = current.next
        return count        
            
llist = LinkedList()
values = list(map(int, input("Enter space-separated numbers: ").split()))

for val in values:
    llist.append(val)
sol = Solution()

length = sol.getCount(llist.head)
print("Length of linked list:", length)


