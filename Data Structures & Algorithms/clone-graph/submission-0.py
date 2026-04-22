"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def copy(cur):
            if not cur:
                return None
            if cur in visited:
                return visited[cur]
            newNode = Node(cur.val)
            visited[cur] = newNode
            nbors = []
            for neighbor in cur.neighbors:
                nbors.append(copy(neighbor))
            newNode.neighbors = nbors
            return newNode
        return copy(node)