# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        orderTrav = []
        def helper(cur):
            if not cur:
                return
            
            helper(cur.left)
            orderTrav.append(cur.val)
            helper(cur.right)

        helper(root)
        return orderTrav[k-1]