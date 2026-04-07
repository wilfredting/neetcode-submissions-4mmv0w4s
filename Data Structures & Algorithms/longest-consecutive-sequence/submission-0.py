class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        num_set = set()

        for num in nums:
            if num not in num_set:
                l = r = num
                while l - 1 in num_set:
                    l -= 1
                while r + 1 in num_set:
                    r += 1
                ans = max(ans, r - l + 1)
                num_set.add(num)

        return ans