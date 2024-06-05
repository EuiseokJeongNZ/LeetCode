class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i >= maxi or j >= maxj or i < 0 or j < 0:
                return 1
            if grid[i][j] == 0:
                return 1
            if grid[i][j] == -1:
                return 0

            grid[i][j] = -1
            ans = 0
            for d in range(4):
                ans += dfs(i + di[d], j + dj[d])

            return ans

        di = [0, 0, -1, 1]
        dj = [-1, 1, 0, 0]
        maxi = len(grid)
        maxj = len(grid[0])

        for i in range(maxi):
            for j in range(maxj):
                if grid[i][j] == 1:
                    return dfs(i, j)

        return 0
