# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def search(node):
            if not node:
                return True, 0
            
            leftResult, leftDepth = search(node.left)
            rightResult, rightDepth = search(node.right)

            return leftResult and rightResult and abs(leftDepth - rightDepth) < 2, max(leftDepth, rightDepth) + 1
        
        ans, _ = search(root)
        return ans