# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    maxi = float('-inf')
    def maxPathSum(self, root):
        def pre_order(root):
            if not root:
                return 0
            l = max(0, pre_order(root.left))
            r = max(0, pre_order(root.right))
            self.maxi = max(self.maxi, root.val+l+r)
            return root.val + max(l,r)
        pre_order(root)
        return self.maxi        