class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n

        for mm in range(m - 2, -1, -1):
            curr = [0] * n
            curr[-1] = 1
            for nn in range(n - 2, -1, -1):
                curr[nn] = curr[nn + 1] + prev[nn]
            prev = curr
        
        return prev[0]