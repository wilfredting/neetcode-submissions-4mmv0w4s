class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                target = num + nums[l] + nums[r]
                if target == 0:
                    ans.append([num, nums[l], nums[r]])
                    l_value = nums[l]
                    while nums[l] == l_value and l < r:
                        l += 1
                    r_value = nums[r]
                    while nums[r] == r_value and l < r:
                        r -= 1
                elif target < 0:
                    l_value = nums[l]
                    while nums[l] == l_value and l < r:
                        l += 1
                else:
                    r_value = nums[r]
                    while nums[r] == r_value and l < r:
                        r -= 1

        return ans