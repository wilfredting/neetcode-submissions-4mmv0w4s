class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        prev = [0] * (COLS + 1)
        prev[COLS - 1] = 1
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                if obstacleGrid[row][col]:
                    prev[col] = 0
                else:
                    prev[col] += prev[col + 1]
        return prev[0]