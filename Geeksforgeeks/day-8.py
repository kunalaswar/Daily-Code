
# Count Linked List Nodes
# Given a singly linked list. The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.

# '''

# #Linked list class
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         '''
# class Solution:
#     # Function to count nodes of a linked list.
#     def getCount(self, head):
#         count = 0
#         current = head
#         while current:
#             count = count+1
#             current = current.next
#         return count        
            
# llist = LinkedList()
# values = list(map(int, input("Enter space-separated numbers: ").split()))

# for val in values:
#     llist.append(val)
# sol = Solution()

# length = sol.getCount(llist.head)
# print("Length of linked list:", length)




# # Node class to create linked list nodes
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # LinkedList class to manage the linked list
# # class LinkedList:
# #     def __init__(self):
# #         self.head = None
# #         self.tail = None

# #     def append(self, data):
# #         new_node = Node(data)
# #         if self.head is None:
# #             self.head = new_node
# #             self.tail = new_node
# #         else:
# #             self.tail.next = new_node
# #             self.tail = new_node

# # # Solution class to count nodes
# # class Solution:
# #     def getCount(self, head):
# #         count = 0
# #         current = head
# #         while current:
# #             count += 1
# #             current = current.next
# #         return count

# # # Main program
# # llist = LinkedList()

# # values = list(map(int, input("Enter space-separated numbers: ").split()))

# # for val in values:
# #     llist.append(val)

# # sol = Solution()
# # length = sol.getCount(llist.head)
# # print("Length of linked list:", length)

