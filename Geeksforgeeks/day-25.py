
# Swap kth elements


def swapKth(arr, k):
        # Code Here
    for i in range(len(arr)):
        n = len(arr)
        if k<=0 and k>n:
            return arr
        arr[k-1],arr[n-k] = arr[n-k],arr[k-1]        
        return arr
    
res = swapKth([1, 2, 3, 4, 5], 2) 
print(res)
        
res1 = swapKth([1, 2, 3, 4, 5, 6, 7, 8], 3)
print(res1)
