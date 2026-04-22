# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, tracker, k):
        if not root:
            return
        
        self.helper(root.left, tracker, k)

        if len(tracker) >= k:
            return
        
        tracker.append(root.val)
        
        self.helper(root.right, tracker, k)
        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        self.helper(root, lst, k)
        return lst[-1]