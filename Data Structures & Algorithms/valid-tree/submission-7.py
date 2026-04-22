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

"""
To check if a directed graph has a cycle, you have to keep track of 
the current path and make sure that you don't hit the same node twice
in the same path. However, to check if an undirected graph has a cycle, 
you just have to skip over the parent as a neighbor node. Then, you
just have to check if you hit the same node twice ever. Once you have ran
this recursion on one node, just check that all of the nodes have been 
processed or else it wouldn't be a connected tree.
""" 