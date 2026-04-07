class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()

        i, j = 0, len(s_lower) - 1

        while (i < j):
            while i < j and not s_lower[i].isalnum():
                i += 1
            while j > i and not s_lower[j].isalnum():
                j -= 1
            if s_lower[i] != s_lower[j]:
                return False
            i += 1
            j -= 1
            
        return True