class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        visited = [[False] * n for _ in range(n)]
        ans = [[1] * n for _ in range(n)]
        drctn = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        r, c = 0, 0
        visited[r][c] = True

        for i in range(0, n ** 2):
            while True:
                nr, nc = drctn[i % 4]
                temp = ans[r][c]
                if 0 <= r + nr < n and 0 <= c + nc < n and not visited[r + nr][c + nc]:
                    r += nr
                    c += nc
                    ans[r][c] = temp + 1
                    visited[r][c] = True
                else:
                    break

        return ans