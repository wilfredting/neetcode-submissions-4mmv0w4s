class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            curr = (r - l) * min(heights[l], heights[r])
            area = max(curr, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area