# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def search(node, mx):
            if not node:
                return 0
            
            sm = search(node.left, max(mx, node.val)) + search(node.right, max(mx, node.val))

            if node.val >= mx:
                sm += 1
            
            return sm
        return search(root, -float('inf'))
        