
#  Sort the string in descending order
class Solution:
    def ReverseSort(self, s): 
        lst = []
        for i in s:
            lst.append(i)
        # lst.sort(reverse= True)
        for i in range(len(lst)):
            for j in range(0,len(lst)-1):
                if lst[j] < lst[j+1]: # ascending order 
                    lst[j],lst[j+1] = lst[j+1],lst[j]


        return ''.join(lst)


s  = Solution()        
print(s.ReverseSort("geeks"))

print(s.ReverseSort("for"))

        