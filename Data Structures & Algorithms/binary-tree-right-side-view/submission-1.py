# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []

        queue = deque([root])
        while queue:
            length = len(queue)
            right = None
            for i in range(length):
                curr = queue.popleft()
                if curr:
                    right = curr.val
                    queue.append(curr.left)
                    queue.append(curr.right)
            if right:
                ans.append(right)
        return ans
        