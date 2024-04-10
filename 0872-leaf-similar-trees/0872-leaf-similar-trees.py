# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []
        def pre_order(root, res):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
            pre_order(root.left, res)
            pre_order(root.right, res)
        pre_order(root1, res1)
        pre_order(root2, res2)
        return res1 == res2
        