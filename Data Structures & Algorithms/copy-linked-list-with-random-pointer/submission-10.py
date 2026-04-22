"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {}

        def copyHelper(head):
            if head is None:
                return None
            if head in mapping:
                return mapping[head]
            
            copy = Node(head.val)
            mapping[head] = copy
            copy.next = copyHelper(head.next)
            copy.random = copyHelper(head.random)
            return copy
        
        return copyHelper(head)

        