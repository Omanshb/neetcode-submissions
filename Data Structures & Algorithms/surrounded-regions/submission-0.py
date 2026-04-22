class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        def helper(x, y):
            if x not in range(len(board)) or y not in range(len(board[0])):
                return False
            
            if board[x][y] == "X" or (x, y) in visited:
                return True
            
            visited.add((x, y))
            
            val = all([helper(x + 1, y), helper(x - 1, y), helper(x, y + 1), helper(x, y - 1)])

            visited.remove((x, y))

            return val
            
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and helper(i, j):
                    board[i][j] = "X"
        