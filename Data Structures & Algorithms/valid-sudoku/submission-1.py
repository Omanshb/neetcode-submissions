class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            for c in row:
                if c.isdigit() and row.count(c) > 1:
                    return False
        
        for j in range(9):
            column = [board[i][j] for i in range(9)]
            for c in column:
                if c.isdigit() and column.count(c) > 1:
                    return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = []
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        block.append(board[x][y])
                for c in block:
                    if c.isdigit() and block.count(c) > 1:
                        return False

        return True
