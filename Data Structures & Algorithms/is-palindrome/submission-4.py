class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()

        i, j = 0, len(s_lower) - 1

        while (i < j):
            while not s_lower[i].isalnum():
                i += 1
                if (i >= j):
                    return True
            while not s_lower[j].isalnum():
                j -= 1
                if (j <= i):
                    return True
            if s_lower[i] != s_lower[j]:
                return False
            i += 1
            j -= 1
            
        return True