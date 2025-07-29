
# 599. Minimum Index Sum of Two Lists
    
class Solution:
    def findRestaurant(self, list1,list2):
        min_sum = float('inf')
        result = []

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    index_sum = i+j
                    if index_sum < min_sum:
                        min_sum = index_sum 
                        result = [list1[i]]
                    elif index_sum == min_sum:
                        result.append(list1[i])    
        return result



s = Solution()
res=s.findRestaurant( list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])
print(res)

res1 = s.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"])
print(res1)
res2 = s.findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"])
print(res2)

# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]