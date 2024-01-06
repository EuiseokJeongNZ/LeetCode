class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex + 1
        dp = [[0 for _ in range(i+1)] for i in range(n)]

        for i in range(n):
            for j in range(i+1):
                if j == 0 or i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        return dp[n - 1]