class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums))
        postfix = [0] * (len(nums))
        for i in range(1, len(nums), 1):
            prefix[i] = nums[i - 1] + prefix[i - 1]
            postfix[-1-i] = nums[-i] + postfix[-i]

        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i

        return -1
            
