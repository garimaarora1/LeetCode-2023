# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        def pre_order(root):
            nonlocal res
            nonlocal k
            if not root:
                return
            pre_order(root.left)
            k -= 1
            if k == 0:
                res = root.val
                return 
            pre_order(root.right)
        pre_order(root)
        return res
        