class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(row, col, cache):
            if min(row, col) < 0 or row == m or col == n:
                return 0
            if cache[row][col]:
                return cache[row][col]
            if row == m - 1 and col == n - 1:
                return 1
            
            cache[row][col] = dfs(row + 1, col, cache) + dfs(row, col + 1, cache)
            return cache[row][col]
        
        return dfs(0, 0, [[0] * n for i in range(m)])