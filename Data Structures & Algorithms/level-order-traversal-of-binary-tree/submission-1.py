# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        curr = deque([root])
        while curr:
            length = len(curr)
            level = []
            for i in range(length):
                node = curr.popleft()
                if node:
                    level.append(node.val)
                    curr.append(node.left)
                    curr.append(node.right)
            if level:
                ans.append(level)
        return ans
        