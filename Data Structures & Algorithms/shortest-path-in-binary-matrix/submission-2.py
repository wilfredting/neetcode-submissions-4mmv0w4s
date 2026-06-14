from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        queue.appendleft((-1, -1))
        path = -1
        while queue:
            path += 1
            for i in range(len(queue)):
                row, col = queue.pop()
                visited.add((row, col))
                if row == ROWS - 1 and col == COLS - 1:
                    return path

                neighbors = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    if (
                        min(nr, nc) < 0
                        or nr == ROWS
                        or nc == COLS
                        or (nr, nc) in visited
                        or grid[nr][nc] == 1
                    ):
                        continue
                    queue.appendleft((nr, nc))

        return -1
