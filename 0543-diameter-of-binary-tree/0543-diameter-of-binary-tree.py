# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def heightOfBinaryTree(root):
            if not root:
                return 0

            left_height = heightOfBinaryTree(root.left)
            right_height = heightOfBinaryTree(root.right)

            self.maxi = max(self.maxi, left_height + right_height)

            return max(left_height, right_height) + 1

        heightOfBinaryTree(root)
        return self.maxi
        
        
        