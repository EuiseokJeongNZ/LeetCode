from collections import deque


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        def bfs(si, sj, ei, ej, health):
            i_length = len(grid)
            j_length = len(grid[0])
            q = deque([])
            visited[0][0] = 1

            if grid[si][sj] == 1:
                health -= 1

            q.append((si, sj, health))

            while q:
                ci, cj, cur_health = q.popleft()
                for d in range(4):
                    ni, nj = ci + di[d], cj + dj[d]
                    if 0 <= ni < i_length and 0 <= nj < j_length:
                        new_health = cur_health
                        if grid[ni][nj] == 1:
                            new_health = cur_health - 1

                        if new_health >= 0 and visited[ni][nj] < new_health:
                            visited[ni][nj] = new_health
                            q.append((ni, nj, new_health))

            return visited[ei][ej]

        i_length = len(grid)
        j_length = len(grid[0])

        visited = [[0] * j_length for _ in range(i_length)]
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]

        bfs(0, 0, i_length - 1, j_length - 1, health)
        print(visited)
        if visited[i_length - 1][j_length - 1] >= 1:
            return True

        return False
