# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    maxi = float('-inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find(root):
            if not root:
                return 0
            l = max(0, find(root.left))
            r = max(0, find(root.right))
            self.maxi = max(self.maxi, root.val+l+r)
            return root.val+max(l,r)
        find(root)
        return self.maxi
        
        return self.maxi
        