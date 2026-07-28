class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        res = k
        L = 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            max_freq = max(max_freq, count[s[R]])
            while R - L + 1 - max_freq > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)

        return res