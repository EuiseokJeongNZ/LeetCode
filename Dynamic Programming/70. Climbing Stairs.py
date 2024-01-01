class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        def recursion(n, dp):
            if n == 1:
                dp[n] = 1
                return 1
            if n == 2:
                dp[2] = 2
                return 2

            if dp[n] != 0: # if the dp memorised the value executed beforehand, return the current value
                return dp[n]

            dp[n] = recursion(n - 1, dp) + recursion(n - 2, dp)
            return dp[n]

        return recursion(n, dp)
