
# 1408. String Matching in an Array

class Solution:
  
    def stringMatching(self, words):
        result = []
        for i in words:
            for j in words:
                if i != j and i in j:
                    result.append(i)
                    break  # No need to check further if already found
        return result



s = Solution()
print(s.stringMatching(["mass","as","hero","superhero"]))

print(s.stringMatching(["leetcode","et","code"]))
print(s.stringMatching(["blue","green","bu"]))
        
