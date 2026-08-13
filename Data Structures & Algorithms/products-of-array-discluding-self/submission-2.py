class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums), 1):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            postfix[-1-i] = postfix[-i] * nums[-i]
            
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]

        return res