class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in nums:
            num_set.add(num)
            if not (num - 1) in num_set:
                longest = 1
                while num + longest in num_set:
                    longest += 1
                ans = max(ans, longest)
        return ans