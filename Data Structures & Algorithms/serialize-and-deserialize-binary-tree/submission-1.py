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
        
        ans = ""

        for node in lst:
            if not node:
                ans += "N"

            else:
                ans += f"{node.val:0{5}}"
        
        return ans

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lst = []
        while data:
            if data[0] == "N":
                lst.append(None)
                data = data[1:]
            else:
                lst.append(TreeNode(int(data[:5])))
                data = data[5:]
        
        for i in range(len(lst) // 2):
            if not lst[i]:
                continue
            else:
                node = lst[i]
                node.left = lst[((i + 1) * 2) - 1]
                node.right = lst[((i + 1) * 2)]
        
        return lst[0] if lst else None
        
