# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = [root.val]

        def helper(cur):
            if not cur:
                return 0
            
            leftMax = helper(cur.left)
            rightMax = helper(cur.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            mx[0] = max(mx[0], cur.val + leftMax + rightMax)

            return cur.val + max(leftMax, rightMax)
        
        helper(root)
        return mx[0]
          