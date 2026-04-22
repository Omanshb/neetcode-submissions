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
            if cur in visited:
                return visited[cur]

            newNode = Node(cur.val)
            visited[cur] = newNode
            newNode.neighbors = []
            for neighbor in cur.neighbors:
                newNode.neighbors.append(copy(neighbor))
            return newNode
        return copy(node) if node else None