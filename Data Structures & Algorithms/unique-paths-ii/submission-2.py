class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        prev = [0] * COLS
        prev[-1] = 1
        for row in range(ROWS - 1, -1, -1):
            curr = [0] * COLS
            curr[-1] = prev[-1] if obstacleGrid[row][-1] == 0 else 0
            for col in range(COLS - 2, -1, -1):
                curr[col] = prev[col] + curr[col + 1] if obstacleGrid[row][col] == 0 else 0
            prev = curr
            print(prev)
        return prev[0]