class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        if M < N:
            text1, text2, M, N = text2, text1, N, M

        prev = [0] * (N + 1)

        for mm in range(M - 1, -1, -1):
            curr = [0] * (N + 1)
            for nn in range(N - 1, -1, -1):
                if text1[mm] == text2[nn]:
                    curr[nn] = 1 + prev[nn + 1]
                else:
                    curr[nn] = max(prev[nn], curr[nn + 1])
            prev = curr

        return prev[0]
