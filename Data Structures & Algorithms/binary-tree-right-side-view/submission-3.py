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

        q = []
        res = []
        q.append(root)

        while q: 
            len_q = len(q)

            # for each node in the level, add its children to the queue. 
            # If the child is the last element in a row, then add it to the result
            # The child is the last element in the row if 
            for i in range(len_q):
                node = q.pop(0)

                if i == len_q - 1:
                    res.append(node.val)
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)

        return res                

