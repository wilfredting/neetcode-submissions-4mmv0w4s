class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            char_map[s[i]] += 1
            char_map[t[i]] -= 1

        return min(char_map.values()) == max(char_map.values()) == 0