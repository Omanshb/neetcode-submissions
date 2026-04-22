class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {i:[] for i in range(n)}
        for x, y in edges:
            adjMap[x].append(y)
            adjMap[y].append(x)
        
        vis = set()
        def explore(node):
            if node in vis:
                return
            
            vis.add(node)
            for neighbor in adjMap[node]:
                explore(neighbor)
            
        ans = 0
        for i in range(n):
            if i not in vis:
                ans += 1
                explore(i)
        
        return ans

"""
Explore a specific node and then all of it's neighbors. Every time you do,
add that node to the visisted set. Then, move on to the next. You are just
going to add 1 to the count every time you get to a node which hasn't been
visited by some component yet.
"""