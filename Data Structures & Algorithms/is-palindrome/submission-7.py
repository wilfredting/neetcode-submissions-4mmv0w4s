class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed_s = ""
        for c in s:
            if c.isalnum():
                trimmed_s += c
        trimmed_s = trimmed_s.lower()

        l = 0
        r = len(trimmed_s) - 1
        while l < r:
            if trimmed_s[l] != trimmed_s[r]:
                return False
            l += 1
            r -= 1
        return True