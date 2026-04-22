class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, par):
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n

"""
Intuition: In order for a graph to be a tree, it must have exactly n - 1 edges. It must not have a cycle.
And it must be fully connected. First, create an adjacency list. Then, you want to recursively just
go through the list a single time and keep track of visited. It should essentially go through every
single node in one go. When recursing, obviously you don't want to go back and forth between two
nodes so you just keep track of a prev node that you don't go to as a part of neighbors.
"""