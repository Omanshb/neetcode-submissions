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