
#  Move All Zeroes to End
def pushZerosToEnd(arr):
    n = len(arr)
    index = 0  # Position to place the next non-zero element

    # Move all non-zero elements to the front
    for i in range(n):
        if arr[i] != 0:
            arr[index] = arr[i]
            index += 1

    # Fill remaining positions with zeroes
    while index < n:
        arr[index] = 0
        index += 1

    return arr


print(pushZerosToEnd([1, 2, 0, 4, 3, 0, 5, 0]))

print(pushZerosToEnd([10, 20, 30]))
print(pushZerosToEnd([0, 0]))

