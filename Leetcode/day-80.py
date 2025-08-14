
# 748. Shortest Completing Word

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
            
        
        required = {}
        for ch in licensePlate.lower():
            if ch.isalpha():
                required[ch] = required.get(ch, 0) + 1

        best_word = None

        
        for word in words:
            word_lower = word.lower()
            match = True
            for letter, count in required.items():
                if word_lower.count(letter) < count:
                    match = False
                    break
            
        
            if match:
                if best_word is None or len(word) < len(best_word):
                    best_word = word

        return best_word
        
s = Solution()        
print(s.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]))
print(s.shortestCompletingWord(licensePlate = "1s3 456", words = ["looks","pest","stew","show"]))
