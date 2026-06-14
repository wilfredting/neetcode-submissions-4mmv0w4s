class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        ROWS, COLS = len(grid), len(grid[0])


        def calcArea(row, col, area):
            if min(row, col) < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            area += 1

            area = max(calcArea(row + 1, col, area), area)
            area = max(calcArea(row - 1, col, area), area)
            area = max(calcArea(row, col + 1, area), area)
            area = max(calcArea(row, col - 1, area), area)

            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = calcArea(row, col, 0)
                    maxArea = max(maxArea, area)

        return maxArea
