from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        for c in t:
            if c not in counter:
                return False
            counter[c] -= 1
            if counter[c] < 0:
                return False
        return counter.total() == 0