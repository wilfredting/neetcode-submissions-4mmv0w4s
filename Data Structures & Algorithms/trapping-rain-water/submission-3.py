class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeight = max(height)
        res = 0

        for h in range(0, maxHeight + 1, 1):
            L, R = 0, len(height) - 1

            while height[L] < h and L < R:
                L += 1
            while height[R] < h and L < R:
                R -= 1
            
            for i in range(L, R + 1, 1):
                if height[i] < h:
                    res += 1
            
        return res