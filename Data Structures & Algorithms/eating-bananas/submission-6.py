import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcHours(piles, rate):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            return hours
        
        slow = 1
        fast = max(piles)
        res = fast
        while slow <= fast:
            m = (slow + fast) // 2
            if calcHours(piles, m) > h:
                slow = m + 1
            else:
                fast = m - 1
                res = m

        return res