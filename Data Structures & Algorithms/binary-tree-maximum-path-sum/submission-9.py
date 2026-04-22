# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = -float('inf')
        def dfs(curr):
            nonlocal mx

            if not curr:
                return 0
            
            # returns the largest integratable path from left and right side
            left = dfs(curr.left)
            right = dfs(curr.right)

            # max options are: mx itself, just the current node, current node combined with the left and right
            # integratable paths, the current node with only the left, or the current node with only the right
            mx = max(mx, curr.val, curr.val + left + right, curr.val + left, curr.val + right)
            
            return max(left + curr.val, right + curr.val, curr.val)
            

        dfs(root)
        return mx


"""
-1

-2       10
-6     -3   -6
"""