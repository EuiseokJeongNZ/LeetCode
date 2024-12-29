class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        c = len(grid)
        r = len(grid[0])
        cnt = 0

        for j in range(r):
            for i in range(c - 1):
                curr = grid[i][j]
                next = grid[i + 1][j]
                if curr >= next:
                    minimum = curr + 1
                    cnt += minimum - next
                    grid[i + 1][j] = minimum

        return cnt
