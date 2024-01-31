from collections import deque


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def bfs(i, j, visited, grid, di, dj):
            max = grid[i][j]
            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                i, j = queue.popleft()
                for m in range(4):
                    ni = i + di[m]
                    nj = j + dj[m]
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        if visited[ni][nj] == 0:
                            queue.append((ni, nj))
                            visited[ni][nj] = 1
                            max += grid[ni][nj]
            return max

        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visited[i][j] = 1

        res = 0
        di = [0, 0, -1, 1]
        dj = [-1, 1, 0, 0]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j] != 0:
                    temp = bfs(i, j, visited, grid, di, dj)
                    if temp > res:
                        res = temp

        return res