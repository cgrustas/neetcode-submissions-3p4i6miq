# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float("-inf")

        def helper(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_sum = max(helper(node.left), 0)
            right_sum = max(helper(node.right), 0)

            self.max_path = max(self.max_path, node.val + left_sum + right_sum)

            return node.val + max(left_sum, right_sum)
                    
        helper(root)
        return self.max_path
