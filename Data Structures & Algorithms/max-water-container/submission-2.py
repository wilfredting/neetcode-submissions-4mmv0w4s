class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        L, R = 0, len(heights) - 1

        while L < R:
            area = max(area, (R - L)*min(heights[R], heights[L]))
            if heights[R] < heights[L]:
                R -= 1
            else:
                L += 1

        return area