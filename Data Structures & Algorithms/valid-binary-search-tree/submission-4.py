# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True

        # The left subtree of every node contains only nodes with keys 
        # less than the node's key.
        if not self.leftSubtreeIsValid(root.left, root.val) or not self.rightSubtreeIsValid(root.right, root.val):
            return False
                
        return self.isValidBST(root.left) and self.isValidBST(root.right)


    def leftSubtreeIsValid(self, root, value):
        if not root: 
            return True

        if root.val >= value:
            return False
        
        return self.leftSubtreeIsValid(root.left, value) and self.leftSubtreeIsValid(root.right, value)
    
    def rightSubtreeIsValid(self, root, value):
        if not root:
            return True
        
        if root.val <= value:
            return False
        
        return self.rightSubtreeIsValid(root.left, value) and self.rightSubtreeIsValid(root.right, value)
