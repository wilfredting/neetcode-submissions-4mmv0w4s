class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        L = 0
        curr_sum = 0

        for R in range(len(nums)):
            curr_sum += nums[R]
            while curr_sum >= target:
                res = min(res, R - L + 1)
                curr_sum -= nums[L]
                L += 1
                    

        return res if res <= len(nums) else 0