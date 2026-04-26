class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()

        def dfs(i, target, combination):
            if target == 0:
                res.add(tuple(combination))
                return
            if i >= len(nums) or target < 0:
                return
            
            dfs(i, target - nums[i], combination + [nums[i]])
            dfs(i + 1, target - nums[i], combination + [nums[i]])
            dfs(i + 1, target, combination)

        dfs(0, target, [])
    
        return [list(ans) for ans in res]
