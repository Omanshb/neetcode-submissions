class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # path keeps track of the ones we've already seen
        path = set()

        def dfs(r, c, i):
            # when i reaches length of word, we have found it
            if i == len(word):
                return True

            # if r, c not in boundary or the new letter doesn't match or already visited, this path doesn't work
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            # add r, c to path
            path.add((r, c))

            # search all 4 ways
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            # remove r, c from path
            path.remove((r, c))
            return res

        # go through and check all of the starting points
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False