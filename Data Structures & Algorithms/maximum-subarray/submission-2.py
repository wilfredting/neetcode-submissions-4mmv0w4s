class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum += n
            maxSum = max(curSum, maxSum)
            curSum = max(curSum, 0)

        return maxSum