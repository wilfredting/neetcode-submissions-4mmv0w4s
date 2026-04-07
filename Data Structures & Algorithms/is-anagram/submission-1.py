class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count, t_count = {}, {}

        for char in s:
            s_count[char] = 1 + s_count.get(char, 0)
        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)
        return t_count == s_count