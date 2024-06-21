class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        temp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp[j][len(matrix) - 1 - i] = matrix[i][j]

        for t in range(len(temp)):
            matrix[t] = temp[t].copy()