
# 748. Shortest Completing Word

class Solution:
    def shortestCompletingWord(self, licensePlate,words):
    
    # Step 1: keep only letters, make them lowercase
        plate = ""
        for ch in licensePlate:
            if ch.isalpha():
                plate += ch.lower()

        # Step 2: function to check if word has all letters
        def has_all_letters(word, plate):
            word = word.lower()
            for letter in plate:
                if word.count(letter) < plate.count(letter):
                    return False
            return True

        # Step 3: find the shortest word that passes the check
        answer = ""
        for word in words:
            if has_all_letters(word, plate):
                if answer == "" or len(word) < len(answer):
                    answer = word

        return answer
        
s = Solution()        
print(s.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]))

print(s.shortestCompletingWord(licensePlate = "1s3 456", words = ["looks","pest","stew","show"]))