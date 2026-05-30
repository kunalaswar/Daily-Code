# String Rotated by 2 Places
# Given two strings s1 and s2. Return true if the string s2 can be obtained by rotating (in any direction) string s1 by exactly 2 places, otherwise, false.
# Note: Both rotations should be performed in same direction chosen initially.

# Examples:
# Input: s1 = "amazon", s2 = "azonam"
# Output: true
# Explanation: "amazon" can be rotated anti-clockwise by two places, which will make it as "azonam".
# Input: s1 = "geeksforgeeks", s2 = "geeksgeeksfor"
# Output: false
# Explanation: If we rotate "geeksforgeeks" by two place in any direction, we won't get "geeksgeeksfor".
# Input: s1 = "ab", s2 = "ab"
# Output: true
# Explanation: If we rotate "ab" by two place in any direction, we always get "ab".

def isRotated(s1, s2):
    if len(s1) != len(s2):
        return False

    if len(s1) <= 2:
        return s1 == s2

        # clockwise rotation by 2
    clockwise = s1[-2:] + s1[:-2]

        # anti-clockwise rotation by 2
    anticlockwise = s1[2:] + s1[:2]

    return s2 == clockwise or s2 == anticlockwise
    
print(isRotated("amazon", s2 = "azonam"))    
print(isRotated("geeksforgeeks", s2 = "geeksgeeksfor"))    
print(isRotated("ab", s2 = "ab"))    
