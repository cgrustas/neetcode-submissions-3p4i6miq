# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if nodes are in different subtrees

        # if one of the nodes is LCA
        if root.val == p.val or root.val == q.val:
            return root

        # if nodes are in different subtrees
        if root.val < max(p.val, q.val) and root.val > min(p.val, q.val):
            return root
        elif root.val < max(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > min(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)

        # if both nodes are in right subtree

        # if one of the nodes is in the root subtree
