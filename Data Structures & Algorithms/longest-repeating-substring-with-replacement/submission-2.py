class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_arr = [0] * 26
        l = res = 0

        for r in range(len(s)):
            char_arr[ord(s[r]) - ord('A')] += 1
            while sum(char_arr) - max(char_arr) > k:
                char_arr[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(sum(char_arr), res)
        
        return res
