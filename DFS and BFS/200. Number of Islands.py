import sys
sys.setrecursionlimit(2000)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x, y, n, m, dx, dy, grid):
            if 0 <= x < n and 0 <= y < m:
                if grid[x][y] == "1":
                    grid[x][y] = "0"
                    for i in range(4):
                        dfs(x + dx[i], y + dy[i], n, m, dx, dy, grid)

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        for i in range(n):  # 0~3 4
            for j in range(m):  # 0~4 5
                if grid[i][j] == "1":
                    dfs(i, j, n, m, dx, dy, grid)
                    cnt += 1
        return cnt