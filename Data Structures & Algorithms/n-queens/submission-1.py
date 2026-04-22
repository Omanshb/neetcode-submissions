class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        rows, cols, d1, d2 = set(), set(), set(), set()
        board = [["."] * n for x in range(n)]
        
        def helper(i, count):
            row = i // n
            col = i % n

            if i >= n * n:
                if count == n:
                    b = ["".join(s) for s in board]
                    ans.append(b)
                return
            
            helper(i + 1, count)

            if row not in rows and col not in cols and col - row not in d1 and n - row - col not in d2:
                board[row][col] = "Q"
                rows.add(row)
                cols.add(col)
                d1.add(col - row)
                d2.add(n - row - col)

                helper(i + 1, count + 1)
                
                board[row][col] = "."
                rows.remove(row)
                cols.remove(col)
                d1.remove(col - row)
                d2.remove(n - row - col)
        
        helper(0, 0)
        return ans