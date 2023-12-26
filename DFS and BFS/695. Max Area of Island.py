from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        di = [0, 0, -1, 1]
        dj = [-1, 1, 0, 0]

        def bfs(i, j, grid, max_i, max_j):
            q = deque()
            q.append((i, j))
            area = 0
            grid[i][j] = 0

            while q:
                i, j = q.popleft()
                area += 1

                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < max_i and 0 <= nj < max_j and grid[ni][nj] == 1:
                        grid[ni][nj] = 0
                        q.append((ni, nj))

            return area

        max_area = 0
        max_i, max_j = len(grid), len(grid[0])

        for i in range(max_i):
            for j in range(max_j):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j, grid, max_i, max_j))

        return max_area
