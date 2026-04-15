class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        t, b = 0, ROWS - 1
        row = -1
        while t <= b:
            row = (t + b) // 2
            if matrix[row][-1] < target:
                t = row + 1
            elif matrix[row][0] > target:
                b = row - 1
            else:
                break

        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        return False