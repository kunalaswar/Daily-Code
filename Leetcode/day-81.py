
class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",                      ".---","-.-",".-..","--","-.","---",".--.","--.-",                  ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        set1 = set()
        
        for word in words:
            transformation = "".join(morse[ord(c) - ord('a')] for c in word)
            set1.add(transformation)
    
        return len(set1)

s = Solution()
print(s.uniqueMorseRepresentations(["gin","zen","gig","msg"]))
print(s.uniqueMorseRepresentations(["a"]))
