# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, node, mx):
        if not node:
            return 0
        
        sm = self.helper(node.left, max(mx, node.val)) + self.helper(node.right, max(mx, node.val))
        if node.val >= mx:
            return sm + 1
        return sm

    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, -float('inf'))
        