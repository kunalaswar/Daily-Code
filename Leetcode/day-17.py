



def singleNumber( nums):
      
    result = 0
    for num in nums:
        result ^= num
    return result

result = singleNumber([2,2,1])
print(result)      