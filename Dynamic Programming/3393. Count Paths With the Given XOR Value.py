from typing import List
from collections import Counter


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        mod = 10 ** 9 + 7
        r = len(grid)
        c = len(grid[0])

        dp = [[Counter() for _ in range(c)] for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if i == 0 and j == 0:
                    dp[i][j][grid[i][j]] += 1
                elif i == 0:
                    for a, freq in dp[i][j - 1].items():
                        dp[i][j][a ^ grid[i][j]] += freq
                elif j == 0:
                    for b, freq in dp[i - 1][j].items():
                        dp[i][j][b ^ grid[i][j]] += freq
                else:
                    for a, freq in dp[i - 1][j].items():
                        dp[i][j][a ^ grid[i][j]] += freq
                    for b, freq in dp[i][j - 1].items():
                        dp[i][j][b ^ grid[i][j]] += freq

        return dp[r - 1][c - 1][k] % mod

        # r = len(grid)
        # c = len(grid[0])
        # dp = [[[] for _ in range(c)] for _ in range(r)]
        # cnt = 0

        # for i in range(r):
        #     for j in range(c):
        #         if i == 0 and j == 0:
        #             dp[i][j].append(grid[i][j])
        #         elif i == 0:
        #             dp[i][j] = [a ^ grid[i][j] for a in dp[i][j - 1]]
        #         elif j == 0:
        #             dp[i][j] = [b ^ grid[i][j] for b in dp[i - 1][j]]
        #         else:
        #             temp = []
        #             for a in dp[i - 1][j]:
        #                 temp.append(a ^ grid[i][j])
        #             for b in dp[i][j - 1]:
        #                 temp.append(b ^ grid[i][j])
        #             dp[i][j] = temp

        # for i in dp[r-1][c-1]:
        #     if i == k:
        #         cnt += 1

        # return cnt
