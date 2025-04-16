


# 83. Remove Duplicates from Sorted List

# def deleteDuplicates( head):
#         current = head
        
#         # Traverse the list
#         while current and current.next:
#             if current.val == current.next.val:
#                 current.next = current.next.next  # Skip the duplicate node
#             else:
#                 current = current.next  # Move to the next node
        
#         return head

# deleteDuplicates()





# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Function to remove duplicates
# def deleteDuplicates(head):
#     current = head
    
#     # Traverse the list
#     while current and current.next:
#         if current.val == current.next.val:
#             current.next = current.next.next  # Skip the duplicate node
#         else:
#             current = current.next  # Move to the next node
    
#     return head

# # Helper function to create a linked list from a list
# def create_linked_list(arr):
#     head = ListNode(arr[0])
#     current = head
#     for val in arr[1:]:
#         current.next = ListNode(val)
#         current = current.next
#     return head

# # Helper function to print the linked list
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.val, end=" -> " if current.next else "")
#         current = current.next
#     print()

# # Create a sample linked list
# arr = [1, 1, 2, 3, 3]
# head = create_linked_list(arr)

# # Before removing duplicates
# print("Original list:")
# print_linked_list(head)

# # Removing duplicates
# head = deleteDuplicates(head)

# # After removing duplicates
# print("List after duplicates removed:")
# print_linked_list(head)
