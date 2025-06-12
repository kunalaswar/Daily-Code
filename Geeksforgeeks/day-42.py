class Solution:
    '''You need to insert the given element at the given index. 
    After inserting the elements at index, elements
    from index onward should be shifted one position ahead.
    You may assume that the array already has sizeOfArray - 1 elements.'''
    
    def insertAtIndex(self, arr, sizeOfArray, index, element):
        if 0 <= index < sizeOfArray:
            arr.insert(index, element)
            # Remove extra element if list exceeds sizeOfArray
            if len(arr) > sizeOfArray:
                arr.pop()
        print(arr)        

sizeOfArray = 6
index = 5
element = 90        
s = Solution() 
s.insertAtIndex([1, 2, 3, 4, 5],sizeOfArray,index,element)


