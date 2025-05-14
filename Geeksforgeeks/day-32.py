
# Maximum product of two numbers


# def maxProduct(arr):
# 		arr.sort()
# 		return max(arr[0] * arr[1] , arr[-1] * arr[-2])

# arr = [1, 4, 3, 6, 7, 0] 
# print(maxProduct(arr))		   
	            
# arr= [1, 100, 42, 4, 23]
# print(maxProduct(arr))		   

# OR

def maxProduct(arr):
    arr.sort(reverse = True)
    return arr[0] * arr[1]

arr = [1, 4, 3, 6, 7, 0] 
print(maxProduct(arr))		   
	            
arr= [1, 100, 42, 4, 23]
print(maxProduct(arr))		   
