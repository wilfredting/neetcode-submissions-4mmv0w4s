class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = [0] * 26

        if len(s) != len(t): return False

        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1
            char_count[ord(t[i]) - ord('a')] -= 1

        return char_count == [0] * 26