class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        n = len(prices)
        dp = [0] * n

        min_price = prices[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return dp[-1]