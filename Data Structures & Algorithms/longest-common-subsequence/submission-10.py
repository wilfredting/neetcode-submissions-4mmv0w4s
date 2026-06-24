class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for i in range(M + 1)]

        for mm in range(M - 1, -1 ,-1):
            for nn in range(N - 1, -1, -1):
                if text1[mm] == text2[nn]:
                    dp[mm][nn] = 1 + dp[mm + 1][nn + 1]
                else:
                    dp[mm][nn] = max(dp[mm + 1][nn], dp[mm][nn + 1])
        
        return dp[0][0]