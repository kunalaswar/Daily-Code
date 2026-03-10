
# Missing in Array


def missingNum( arr):
        # code here

    for i in range(1,len(arr)+1):
        if i not in arr:
            return i
    return len(arr) + 1




print(missingNum( arr=[1, 2, 3, 5]))
print(missingNum( arr=[8, 2, 4, 5, 3, 7, 1]))
print(missingNum( arr= [1]))


        