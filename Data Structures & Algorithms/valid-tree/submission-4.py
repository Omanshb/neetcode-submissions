class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = {i:[] for i in range(n)}
        for x, y in edges:
            adjMap[x].append(y)
            adjMap[y].append(x)
        
        vis = set()

        def cycleCheck(node, parent):
            if node in vis:
                return True
            vis.add(node)
            for neighbor in adjMap[node]:
                if neighbor == parent:
                    continue
                if cycleCheck(neighbor, node):
                    return True
            return False
        
        if cycleCheck(0, None):
            return False
        if len(vis) < n:
            return False
        
        return True