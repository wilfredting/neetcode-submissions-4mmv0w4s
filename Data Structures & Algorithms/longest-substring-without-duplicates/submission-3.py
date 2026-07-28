class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        L = 0
        seen_char = set()

        for R in range(len(s)):
            while s[R] in seen_char:
                seen_char.remove(s[L])
                L += 1
            seen_char.add(s[R])
            res = max(res, len(seen_char))

        return res