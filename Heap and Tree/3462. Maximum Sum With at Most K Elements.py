import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        h = []

        for i in range(n):
            not_exceed = limits[i]
            temp = []
            for j in range(m):
                heapq.heappush(temp, -grid[i][j])

            for j in range(not_exceed):
                min_pop = heapq.heappop(temp)
                heapq.heappush(h, min_pop)

        for _ in range(k):
            ans += -heapq.heappop(h)

        return ans