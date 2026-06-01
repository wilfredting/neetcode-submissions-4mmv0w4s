class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], index]
            if num not in seen:
                seen[num] = index
        return [-1, -1]
