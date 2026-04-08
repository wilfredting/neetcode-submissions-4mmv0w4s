class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = curr = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            result = max(result, curr)
        return result