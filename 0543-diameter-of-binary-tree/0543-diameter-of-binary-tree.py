# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxi = 0
    def find_height(self, root):
            if not root:
                return 0

            l = self.find_height(root.left)
            r = self.find_height(root.right)
            self.maxi = max(self.maxi, l+r)
            return max(l,r) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.find_height(root)
        return self.maxi