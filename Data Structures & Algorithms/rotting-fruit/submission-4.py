class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        counter = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    queue.append((x, y))
                if grid[x][y] == 1:
                    counter += 1
        
        time = 0
        while counter > 0 and queue:
            length = len(queue)
            for i in range(length):
                x, y = queue.popleft()

                if x + 1 in range(len(grid)) and grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    queue.append((x + 1, y))
                    counter -= 1

                if x - 1 in range(len(grid)) and grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    queue.append((x - 1, y))
                    counter -= 1
                
                if y + 1 in range(len(grid[0])) and grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    queue.append((x, y + 1))
                    counter -= 1
                
                if y - 1 in range(len(grid[0])) and grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    queue.append((x, y - 1))
                    counter -= 1
            time += 1
        
        return time if counter == 0 else -1 

"""
Intuition: Start off with a queue and a counter. The queue has a list of all of the rotten fruits.
The counter is the initial number of fresh fruit that are there on the grid. Then, use BFS using this queue
and keep removing the count every time you contaminate a new fruit. Keep doing the BFS and iterating time
until the count finally reaches 0 or the queue is done. Then, just return the current time. 
"""
