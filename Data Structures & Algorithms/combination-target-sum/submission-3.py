class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def dfs(i, curr, res):
            if sum(curr) == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or sum(curr) > target:
                return

            curr.append(nums[i])
            dfs(i, curr, res)
            curr.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, curr, res)

        res = []
        dfs(0, [], res)
        return res
