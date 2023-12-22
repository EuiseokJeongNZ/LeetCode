class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def condition1(grid):  # each row contains 1 to 9 not duplicated
            for i in range(len(grid)):
                digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                for j in range(len(grid)):
                    if grid[i][j] in digit:
                        digit.remove(grid[i][j])
                    elif grid[i][j] == ".":
                        continue
                    else:
                        return False
            return True

        def condition2(grid):  # each column contains 1 to 9 not duplicated
            for i in range(len(grid)):
                digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                for j in range(len(grid)):
                    if grid[j][i] in digit:
                        digit.remove(grid[j][i])
                    elif grid[j][i] == ".":
                        continue
                    else:
                        return False
            return True

        def condition3(grid): # each of the nine 3*3 sub boxes contains 1 to 9 not duplicated
            for a in range(0, 7, 3):
                for b in range(0, 7, 3):
                    digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                    for i in range(3):
                        for j in range(3):
                            if grid[i+a][j+b] in digit:
                                digit.remove(grid[i+a][j+b])
                            elif grid[i+a][j+b] == ".":
                                continue
                            else:
                                return False
            return True

        return condition1(board) and condition2(board) and condition3(board)