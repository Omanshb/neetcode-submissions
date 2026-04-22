# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def search(node):
            if not node:
                return 0, 0
            
            left, left_mx = search(node.left)
            right, right_mx = search(node.right)

            return max(left, right) + 1, max([left_mx, right_mx, left + right])
        
        _, ans = search(root)
        return ans

            
