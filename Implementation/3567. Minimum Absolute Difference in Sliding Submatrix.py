class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = []

        for i in range(m-k+1):
            temp = []
            for j in range(n-k+1):
                submatrix = [grid[mi][nj] for mi in range(i, i+k) for nj in range(j, j+k)]
                submatrix = sorted(set(submatrix))

                if len(submatrix) == 1:
                    temp.append(0)
                else:
                    min_diff = float('inf')
                    for s in range(len(submatrix) - 1):
                        min_diff = min(min_diff, submatrix[s+1] - submatrix[s])
                    temp.append(min_diff)
            ans.append(temp)

        return ans