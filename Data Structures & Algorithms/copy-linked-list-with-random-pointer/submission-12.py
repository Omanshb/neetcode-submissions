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

        def helper(head):
            if not head:
                return None
            
            if head in mapping:
                return mapping[head]
            
            new = Node(head.val)
            mapping[head] = new
            new.next = helper(head.next)
            new.random = helper(head.random)
            return new
        
        return helper(head)

"""
Intuition: There are two approaches to this problem. The first one is that you start
by just creating a dictionary of every Node : copy Node. Then, you go through each of the
original nodes one by one again and for every .next and every .random, you use the
values from the copy Node in the dictionary to congigure it. The second approach is
that you keep a map and then create a recursive helper function. Obviously, the base
case is that head is None or that head is already in the mapping dictionary. Then, you
create a new copy, map the original to the copy, and then set the copy.next and copy.random
to the values of copyHelper on those. At the end, just return the copy of the original head.
"""
        