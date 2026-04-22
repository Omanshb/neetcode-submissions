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