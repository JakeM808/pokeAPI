# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:				
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

ransomNote = "Well would you look at that"
magazine = "jfkdljaf;sdf;as;flkajd;kfjsa;dfjdkwue09wuj"


def solution(ransomNote, magazine):
    for chr in set(ransomNote):
        if ransomNote.count(chr) > magazine.count(chr):
            return False
        else:
            return True
        
