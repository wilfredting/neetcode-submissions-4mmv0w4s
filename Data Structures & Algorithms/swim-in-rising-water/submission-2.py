import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        shortest = {}
        minHeap = [(grid[0][0], 0, 0)]
        while minHeap:
            w1, r1, c1 = heapq.heappop(minHeap)
            if (r1, c1) in shortest:
                continue
            shortest[(r1, c1)] = w1
            if (r1, c1) == (ROWS-1, COLS-1):
                return w1

            for delta_r, delta_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r = r1 + delta_r
                new_c = c1 + delta_c
                if min(new_r, new_c) < 0 or new_r >= ROWS or new_c >= COLS or (new_r, new_c) in shortest:
                    continue
                heapq.heappush(minHeap, (max(w1, grid[new_r][new_c]), new_r, new_c))
        
        return -1