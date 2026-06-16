class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1, dp2 = 0, 0
        for num in nums:
            temp = max(dp1 + num, dp2)
            dp1 = dp2
            dp2 = temp

        return dp2