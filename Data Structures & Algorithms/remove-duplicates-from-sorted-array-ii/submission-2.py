class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        prev1, prev2 = -10001, -math.inf

        for R in range(len(nums)):
            if not (prev1 == prev2 == nums[R]):
                nums[L] = nums[R]
                L += 1

            prev1, prev2 = nums[R], prev1
        
        return L
