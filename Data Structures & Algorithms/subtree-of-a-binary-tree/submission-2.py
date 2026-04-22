# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(t1, t2):
            if not (t1 or t2):
                return True
            if not (t1 and t2):
                return False
            return t1.val == t2.val and helper(t1.left, t2.left) and helper(t1.right, t2.right)
        
        def check(curr):
            if helper(curr, subRoot):
                return True
            if not curr:
                return False
            return check(curr.left) or check(curr.right)
        
        return check(root)
            