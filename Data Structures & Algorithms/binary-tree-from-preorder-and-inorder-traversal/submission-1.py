# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {inorder[x] : x for x in range(len(inorder))}
        counter = 0

        def search(left, right):
            nonlocal counter
            if left > right:
                return
            
            curr = TreeNode(preorder[counter])
            counter += 1

            curr.left = search(left, index[curr.val] - 1)
            curr.right = search(index[curr.val] + 1, right)
            
            return curr

        return search(0, len(preorder) - 1)