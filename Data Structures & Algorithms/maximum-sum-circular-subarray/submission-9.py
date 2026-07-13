class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = nums[0]
        globalMax = nums[0]
        currMin = nums[0]
        globalMin = nums[0]
        totalSum = nums[0]

        for i in range(1, len(nums), 1):
            n = nums[i]
            currMax = max(currMax + n, n)
            globalMax = max(currMax, globalMax)
            currMin = min(currMin + n, n)
            globalMin = min(currMin, globalMin)
            totalSum += n

        return max(totalSum - globalMin, globalMax) if globalMax >= 0 else globalMax
