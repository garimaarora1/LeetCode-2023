# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0 or root.val == 1:
            return root.val
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)
        if root.val == 2:
            if l == 1 or r == 1:
                return True
            else:
                return False
        elif root.val == 3:
            if l == 0 or r == 0:
                return False
            else:
                return True