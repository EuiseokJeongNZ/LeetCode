from collections import deque


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def bfs(i, j, grid, visited, di, dj):
            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1
            while queue:
                i, j = queue.popleft()
                for m in range(4):
                    ni = i + di[m]
                    nj = j + dj[m]
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        if visited[ni][nj] == 0 and grid[ni][nj] == 1:
                            queue.append((ni, nj))
                            visited[ni][nj] = 1
            lst = [i, j]
            return lst

        res = []
        di = [0, 0, -1, 1]
        dj = [1, -1, 0, 0]
        visited = [[0] * len(land[0]) for _ in range(len(land))]

        for i in range(len(land)):
            for j in range(len(land[0])):
                if visited[i][j] == 0 and land[i][j] == 1:
                    temp = [i, j]
                    temp += bfs(i, j, land, visited, di, dj)
                    res.append(temp)
        return res
