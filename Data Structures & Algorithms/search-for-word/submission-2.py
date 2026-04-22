class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        path = set()

        def helper(x, y, st):
            nonlocal ans
            if x >= len(board) or y >= len(board[0]) or x < 0 or y < 0 or (x, y) in path:
                return

            st += board[x][y]
            path.add((x, y))

            if len(st) >= len(word):
                if st == word:
                    ans = True
                path.remove((x, y))
                return

            helper(x + 1, y, st)
            helper(x - 1, y, st)
            helper(x, y + 1, st)
            helper(x, y - 1, st)
            path.remove((x, y))

        for x in range(len(board)):
            for y in range(len(board[0])):
                helper(x, y, "")

        return ans