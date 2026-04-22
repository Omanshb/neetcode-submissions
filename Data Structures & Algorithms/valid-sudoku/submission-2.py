class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {x:set() for x in range(0, 9)}
        columns = {x:set() for x in range(0, 9)}
        boxes = {x:set() for x in range(0, 9)}

        for i in range(0, 9):
            for j in range(0, 9):
                val = board[i][j]

                if val == ".":
                    continue
                
                if val in rows[j] or val in columns[i] or val in boxes[(j // 3) + (3 * (i // 3))]:
                    return False
                
                rows[j].add(val)
                columns[i].add(val)
                boxes[(j // 3) + (3 * (i // 3))].add(val)
        
        return True