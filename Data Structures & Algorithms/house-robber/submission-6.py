class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp1, dp2 = nums[0], max(nums[0], nums[1])

        i = 2
        while i < len(nums):
            tmp = dp2
            dp2 = max(dp1 + nums[i], dp2)
            dp1 = tmp
            i += 1
        
        return dp2