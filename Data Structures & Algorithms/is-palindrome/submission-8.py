class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed_s = s.lower()

        l = 0
        r = len(trimmed_s) - 1
        while l < r:
            while not trimmed_s[l].isalnum() and l < r:
                l += 1
            while not trimmed_s[r].isalnum() and l < r:
                r-=1

            if trimmed_s[l] != trimmed_s[r]:
                return False
                
            l += 1
            r -= 1
        return True