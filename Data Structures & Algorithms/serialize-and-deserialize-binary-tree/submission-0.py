# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        lst = []
        
        queue = deque([root])
        while queue:
            length = len(queue)
            found = False
            level = []
            for i in range(length):
                curr = queue.popleft()
                level.append(curr)
                if curr:
                    found = True
                    queue.append(curr.left)
                    queue.append(curr.right)
                else:
                    queue.append(None)
                    queue.append(None)
        
            if not found:
                break
            lst += level
        
        binary = ""

        for node in lst:
            if not node:
                binary += "1"

            else:
                binary += f"{node.val:0{10}b}"
        
        return binary

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lst = []
        while data:
            if data[0] == "1":
                lst.append(None)
                data = data[1:]
            else:
                lst.append(TreeNode(int(data[:10], 2)))
                data = data[10:]
        
        for i in range(len(lst) // 2):
            if not lst[i]:
                continue
            else:
                node = lst[i]
                node.left = lst[((i + 1) * 2) - 1]
                node.right = lst[((i + 1) * 2)]
        
        return lst[0] if lst else None
        
