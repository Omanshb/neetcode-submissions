"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cp = {}
        def helper(curr):
            if not curr:
                return curr
            if curr in cp:
                return cp[curr]
            
            newnode = Node(curr.val)
            cp[curr] = newnode
            newnode.neighbors = [helper(x) for x in curr.neighbors]

            return newnode
        
        return helper(node)

"""
Intuition: Our helper will essentially make a copy of the current node and then
the neighbors of this current node will be helper(x) for each of the neighbors the
node has. If the neighbor is None or if the node is already copied, we can just
use the copied version of it from the cache.
"""
