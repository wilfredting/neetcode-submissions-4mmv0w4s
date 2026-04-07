class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_arr = [0] * 26
        l = res = 0

        for r in range(len(s)):
            max_val = max(char_arr)
            total_val = sum(char_arr)
            while total_val - max_val > k:
                char_arr[ord(s[l]) - ord('A')] -= 1
                l += 1
                max_val = max(char_arr)
                total_val = sum(char_arr)
            char_arr[ord(s[r]) - ord('A')] += 1
            max_val = max(char_arr)
            total_val = sum(char_arr)
            if total_val - max_val <= k:
                res = max(sum(char_arr), res)
        
        return res
