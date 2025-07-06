
#  162. Find Peak Element

def findPeakElement(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            # Peak must be on the left (including mid)
            right = mid
        else:
            # Peak must be on the right
            left = mid + 1

    return left  # or right, both are same here

print(findPeakElement([1,2,3,1]))
print(findPeakElement([1,2,1,3,5,6,4]))