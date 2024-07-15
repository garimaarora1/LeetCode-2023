# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def _maxPathSum(root):
            if not root:
                return 0
            left_path = max(_maxPathSum(root.left), 0)
            right_path = max(_maxPathSum(root.right), 0)
            self.maxi = max(self.maxi, left_path + right_path + root.val)

            return max(left_path, right_path) + root.val
        
        _maxPathSum(root)
        return self.maxi
        