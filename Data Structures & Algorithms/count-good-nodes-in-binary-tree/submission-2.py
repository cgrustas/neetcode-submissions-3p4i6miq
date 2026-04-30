# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_value = float("-inf")

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelp(root, root.val)


    def goodNodesHelp(self, root: TreeNode, max_value: int) -> int:
        if not root: 
            return 0
        
        max_value = max(max_value, root.val)
        if root.val == max_value: 
            return 1 + self.goodNodesHelp(root.left, max_value) + self.goodNodesHelp(root.right, max_value)
        else:
            return self.goodNodesHelp(root.left, max_value) + self.goodNodesHelp(root.right, max_value)
