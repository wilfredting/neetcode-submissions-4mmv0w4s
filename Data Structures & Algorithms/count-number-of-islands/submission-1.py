class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])


        def deleteIsland(row, col):
            if min(row, col) < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            deleteIsland(row + 1, col)
            deleteIsland(row - 1, col)
            deleteIsland(row, col + 1)
            deleteIsland(row, col - 1)

            return

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    deleteIsland(row, col)
                    count += 1

        return count