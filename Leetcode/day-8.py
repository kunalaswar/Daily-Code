# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        bracket_dict = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_dict:
                top_ele = lst.pop() if lst else "_"
                if bracket_dict[char] !=top_ele:
                    return False
            else:
                lst.append(char)        
        return not lst


s = Solution()

print(s.isValid("()"))        # True
print(s.isValid("()[]{}"))    # True
print(s.isValid("(]"))        # False
print(s.isValid("([)]"))      # False
