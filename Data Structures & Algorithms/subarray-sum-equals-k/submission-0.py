class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {}
        count[0] = 1

        res = 0
        prefix = 0

        for num in nums:
            prefix += num
            target = prefix - k
            res += count.get(target, 0)
            count[prefix] = count.get(prefix, 0) + 1

        return res