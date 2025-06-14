# 121. Best Time to Buy and Sell Stock

def containsNearbyDuplicate(nums, k):
    seen = {}  # Dictionary to store number and its last seen index

    for i in range(len(nums)):
        num = nums[i]

        if num in seen:
            if i - seen[num] <= k:
                return True  # Found two indices with same value and within k distance

        # Update the latest index of the number
        seen[num] = i

    return False  # No such pair found



print(containsNearbyDuplicate([1, 2, 3, 1], 3))  # True
print(containsNearbyDuplicate([1, 0, 1, 1], 1))  # True
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # False
