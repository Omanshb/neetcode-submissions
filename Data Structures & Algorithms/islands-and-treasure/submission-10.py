class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def helper(x, y, c):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] < c:
                return
            
            grid[x][y] = c


            helper(x - 1, y, c + 1)
            helper(x + 1, y, c + 1)
            helper(x, y - 1, c + 1)
            helper(x, y + 1, c + 1)
        
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 0:
                    helper(x, y, 0)

"""
Intuition: Instead of trying to search for the treasure spots from any given
grid square, we do the opposite. We start at the treasure spots and from each
of them, we perform DFS outwards while keeping a c as the current distance away
from the treasure. If the current square has a value already less than c, no need 
to change it. Otherwise, please change that grid value to c as the most up to date
distance from any treasure. Inherently, this also resolves any repitition of squares
that might be possible.
"""
        
        