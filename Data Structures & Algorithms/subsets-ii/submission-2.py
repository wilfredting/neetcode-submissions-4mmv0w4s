class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def dfs(i, subset, res):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1, subset, res)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i +=  1

            dfs(i + 1, subset, res)

        res = []
        dfs(0, [], res)
        return res