class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        visited = [[False] * len(board[0]) for x in range(len(board))]
        def helper(x, y, st):
            nonlocal ans
            if x >= len(board) or y >= len(board[0]) or x < 0 or y < 0 or visited[x][y]:
                return
            
            st += board[x][y]
            visited[x][y] = True

            if len(st) >= len(word):
                if st == word:
                    ans = True
                visited[x][y] = False
                return
            
            helper(x + 1, y, st)
            helper(x - 1, y, st)
            helper(x, y + 1, st)
            helper(x, y - 1, st)
            visited[x][y] = False
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                helper(x, y, "")
        
        return ans