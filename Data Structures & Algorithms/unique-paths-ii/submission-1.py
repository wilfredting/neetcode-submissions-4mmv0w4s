class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        def dfs(row, col, cache):
            if min(row, col) < 0 or row == ROWS or col == COLS or obstacleGrid[row][col] == 1:
                return 0
            if cache[row][col] > -1:
                return cache[row][col]
            if row == ROWS - 1 and col == COLS - 1:
                return 1
            
            cache[row][col] = dfs(row + 1, col, cache) + dfs(row, col + 1, cache)
            return cache[row][col]

        return dfs(0, 0, [[-1] * COLS for i in range(ROWS)])