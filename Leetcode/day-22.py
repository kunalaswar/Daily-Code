
# 88. Merge Sorted Array


class Solution:
    def merge(self, nums1,nums2,m,n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]

        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                if nums1[i]>nums1[j]:
                    nums1[i],nums1[j]  = nums1[j],nums1[i] 
        print(nums1)


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s = Solution()
s.merge(nums1,nums2,3,3)

#*  
def merge(nums1,num2,m,n):
    for i in range(n):
        nums1[m+i] = nums2[i]
    # print(nums1)    
    nums1.sort()
    print(nums1)


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1,nums2,3,3)

#* 

def merge(nums1,nums2,m, n):
    nums1[m:] = nums2    
    nums1.sort() 
    print(nums1)        

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1,nums2,3,3)












        