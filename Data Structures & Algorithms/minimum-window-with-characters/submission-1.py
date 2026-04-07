class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)

        for c in t:
            t_count[c] += 1

        have = 0
        need = len(t_count)
        l = ans_l = 0
        ans_r = float('inf')
        for r in range(len(s)):
            t_count[s[r]] -= 1
            if t_count[s[r]] == 0:
                have += 1
            while have == need:
                if ans_r - ans_l > r - l:
                    ans_r, ans_l = r, l
                t_count[s[l]] += 1
                if t_count[s[l]] == 1:
                    have -= 1
                l += 1
 
        return "" if ans_r == float('inf') else s[ans_l:ans_r + 1]