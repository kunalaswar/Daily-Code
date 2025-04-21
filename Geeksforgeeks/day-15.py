
def findPosition(k, arr):
    for i in range(len(arr)):
        if arr[i] == k:
            return i + 1 
    return -1  

k = 98
arr = [1, 22, 57, 47, 34, 18, 66]
print(findPosition(k, arr)) 
