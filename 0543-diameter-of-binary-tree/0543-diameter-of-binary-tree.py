# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def _diameterOfBinaryTree(root):
            if not root:
                return 0

            left_height = _diameterOfBinaryTree(root.left)
            right_height = _diameterOfBinaryTree(root.right)

            self.maxi = max(self.maxi, left_height + right_height)

            return max(left_height, right_height) + 1

        _diameterOfBinaryTree(root)
        return self.maxi
        
        
        