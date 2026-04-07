class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        num_set = set(nums)

        for num in nums:
            if num - 1 not in num_set:
                next_num = num + 1
                while next_num in num_set:
                    next_num += 1
                ans = max(ans, next_num - num)

        return ans