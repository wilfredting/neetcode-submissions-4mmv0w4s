class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Initialize dp array with -1 for memoization
        dp = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        def dfs(t1, t2):
            # Base case: if we're out of bounds, return 0
            if t1 == len(text1) or t2 == len(text2):
                return 0
            
            # If this subproblem has been solved, return the cached value
            if dp[t1][t2] != -1:
                return dp[t1][t2]

            # If characters match, add 1 to the result and move both indices
            if text1[t1] == text2[t2]:
                dp[t1][t2] = 1 + dfs(t1 + 1, t2 + 1)
            else:
                # Otherwise, try both options (skip one character from text1 or text2)
                dp[t1][t2] = max(dfs(t1 + 1, t2), dfs(t1, t2 + 1))
            
            return dp[t1][t2]

        # Start the DFS from the beginning of both strings
        return dfs(0, 0)