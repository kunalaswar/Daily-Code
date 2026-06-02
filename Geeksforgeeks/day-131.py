# Make the array beautiful





def makeBeautiful(arr):

    stack = []

    for num in arr:

        if stack and ((stack[-1] >= 0 and num < 0) or
                          (stack[-1] < 0 and num >= 0)):

            stack.pop()

        else:

            stack.append(num)

    return stack
print(makeBeautiful([4, 2,-2, 1]))
print(makeBeautiful([2,-2, -1, 1]))