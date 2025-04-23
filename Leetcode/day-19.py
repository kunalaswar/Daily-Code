
# 744. Find Smallest Letter Greater Than Target


# class Solution:
#     def nextGreatestLetter(self, letters,target):
#         for val in letters:
#             if ord(val) > ord(target):
#                 return val
#         return letters[0]        

# s = Solution()
# print(s.nextGreatestLetter(["c","f","j"],"c"))


#OR 

# def nextGreatestLetter(letters,target):
#     i = 0
#     while(i < len(letters)):
#         if letters[i]>target:
#             return letters[i]
#         i = i+1
#     return letters[0]       

# letters =["c","f","j"]
# target = "a"
# s = nextGreatestLetter(letters,target)
# print(s)

#OR
# Binary search Approach

def nextGreatestLetter(letters,target):
    start = 0
    end = len(letters)-1
    while start<=end:
        mid = (start + end)//2
        if letters[mid] >target:
            end = mid -1
        else:
            start = mid +1

    return letters[start %len(letters)]            

letters =["c","f","j"]
target = "a"
s = nextGreatestLetter(letters,target)
print(s)