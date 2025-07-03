
#  Rearranging array

class Solution:    
    def Rearrange(self, arr):
        # Step 1: Sort the array in ascending order
        arr.sort()
        
        # Step 2: Use two pointers to select smallest and largest elements alternately
        i = 0
        j = len(arr) - 1
        lst = []
        
        while i <= j:
            if i == j:
                lst.append(arr[i])  # Middle element (only once)
            else:
                lst.append(arr[i])  # Smallest available
                lst.append(arr[j])  # Largest available
            i += 1
            j -= 1
        
        # Step 3: Copy rearranged values back to original array
        for k in range(len(arr)):
            arr[k] = lst[k]
        
        return arr
    

s = Solution()    
print(s.Rearrange([4,5,1,2,3]))

print(s.Rearrange([1,2,3,4]))