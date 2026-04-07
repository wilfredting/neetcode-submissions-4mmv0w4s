class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)

        for c in t:
            t_count[c] += 1

        def isValidSubstring(sub_count):
            for c in t_count:
                if t_count[c] > sub_count[c]:
                    return False
            return True

        substring_count = defaultdict(int)
        ans = ""
        l = 0
        for r in range(len(s)):
            substring_count[s[r]] += 1
            while isValidSubstring(substring_count):
                if isValidSubstring(substring_count) and (ans == "" or len(ans) > r - l):
                    ans = s[l:r + 1]
                substring_count[s[l]] -= 1
                l += 1
 
        return ans