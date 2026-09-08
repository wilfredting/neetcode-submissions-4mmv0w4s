class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i, comb, res, n, k):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for j in range(i, n + 1):
                comb.append(j)
                dfs(j + 1, comb, res, n, k)
                comb.pop()
        
        res = []
        dfs(1, [], res, n, k)
        return res