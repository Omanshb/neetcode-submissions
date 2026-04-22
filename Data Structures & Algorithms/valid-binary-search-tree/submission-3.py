# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(curr, lowerlim, upperlim):
            if not curr:
                return True
            elif curr.val <= lowerlim or curr.val >= upperlim:
                return False
            return all([helper(curr.left, lowerlim, curr.val), helper(curr.right, curr.val, upperlim)])
        return helper(root, float('-inf'), float('inf'))