class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3
        for n in nums:
            counter[n] += 1
        
        curr = 0
        for i in range(3):
            while counter[i]:
                nums[curr] = i
                curr += 1
                counter[i] -= 1