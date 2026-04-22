# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(cur, lowerlim, upperlim):
            if not cur:
                return True
            if cur.val >= upperlim or cur.val <= lowerlim:
                return False
            return all([helper(cur.left, lowerlim, cur.val), helper(cur.right, cur.val, upperlim)])
        return helper(root, -float('inf'), float('inf'))