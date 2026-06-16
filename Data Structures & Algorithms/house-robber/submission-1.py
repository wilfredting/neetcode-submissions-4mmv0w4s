class Solution:
    def __init__(self):
        self.cache = {}

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        if len(nums) in self.cache:
            return self.cache[len(nums)]

        self.cache[len(nums)] = max(self.rob(nums[0:-1]), self.rob(nums[0:-2]) + nums[-1])

        return self.cache[len(nums)]