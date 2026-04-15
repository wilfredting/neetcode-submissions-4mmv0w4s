class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [item for row in matrix for item in row]
        
        l = 0
        r = len(flat) - 1

        while l <= r:
            m = int((l + r) / 2)
            if flat[m] < target:
                l = m + 1
            elif flat[m] > target:
                r = m - 1
            else:
                return True
        return False