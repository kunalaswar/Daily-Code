
# 496. Next Greater Element I


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        
        result = []

        for num in nums1:        
            index_in_nums2 = nums2.index(num)       
        
            found = -1
            for i in range(index_in_nums2 + 1, len(nums2)):
                if nums2[i] > num:
                    found = nums2[i]
                    break
        
        
            result.append(found)

        return result

s = Solution()
print(s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))

print(s.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))

        

