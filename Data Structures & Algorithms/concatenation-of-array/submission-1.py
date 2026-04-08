class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nlen = len(nums)
        ans = [0] * 2 * nlen

        for i, num in enumerate(nums):
            ans[i] = num
            ans[i + nlen] = num

        return ans