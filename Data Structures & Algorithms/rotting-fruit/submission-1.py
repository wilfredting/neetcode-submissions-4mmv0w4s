from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = set()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.appendleft((row, col))
                elif grid[row][col] == 1:
                    fresh.add((row, col))

        minutes = -1
        while queue:
            minutes += 1
            for i in range(len(queue)):
                row, col = queue.pop()

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc

                    if (nr, nc) in fresh:
                        fresh.remove((nr, nc))
                        queue.appendleft((nr, nc))

        return max(minutes, 0) if len(fresh) == 0 else -1
