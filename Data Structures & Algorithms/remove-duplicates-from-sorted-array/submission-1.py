class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        prev = -101
        
        for R in range(len(nums)):
            if nums[R] != prev:
                prev = nums[R]
                nums[L] = prev
                L += 1
        
        return L

