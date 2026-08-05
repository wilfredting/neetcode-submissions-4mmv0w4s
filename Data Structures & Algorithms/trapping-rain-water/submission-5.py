class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        maxL, maxR = 0, 0
        res = 0

        while L <= R:
            i = L if maxL <= maxR else R
            res += max(min(maxL, maxR) - height[i], 0)
            if maxL <= maxR:
                maxL = max(maxL, height[L])
                L += 1
            else:
                maxR = max(maxR, height[R])
                R -= 1


        return res