# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"
        
        q = deque([])
        res = []

        q.append(root)
        while q:
            node = q.popleft()
            if node: 
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        node_values = data.split(",")

        if node_values and node_values[0] == "null":
            return None
        
        q = deque([])
        root = TreeNode(int(node_values[0]))
        q.append(root)
        i = 1 # we start at 1 since the root is already processed at 0 

        while q: 
            node = q.popleft()
            # append left child 
            if node_values[i] != "null":
                node.left = TreeNode(int(node_values[i]))
                q.append(node.left)
            i += 1

            # append right child
            if node_values[i] != "null":
                node.right = TreeNode(int(node_values[i]))
                q.append(node.right)
            i += 1
        return root
            
        
    
