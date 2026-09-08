class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, subset, res):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1, subset, res)
            subset.pop()
            dfs(i + 1, subset, res)
            
        res = []
        dfs(0, [], res)
        return res