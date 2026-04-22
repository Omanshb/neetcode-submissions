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

"""
Intuition: Essentially, you just need a set for every row, column, and box that's possible. Then,
once you have initialized these, you will need to iterate over the entire sudoku grid. To add to the
right row, you simply use the value of j. To add to the right column, you simply use the value of i. 
To add to the right box, you can use a tuple like (i // 3, j // 3) but I just used a simple calculation
(j // 3) + (3 * (i // 3)) which orders the boxes from 0 to 9 respectively. 

Time Complexity: O(n) becuase we just iterate through the sudoku grid once and checking for existence
in a set is O(1)
Space Complexity: O(n^2) because we have to store every row, column, and box, leading to 3 * 9^2 spaces used.
"""