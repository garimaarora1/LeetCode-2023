# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxi = float('-inf')
        
        def pre_order(root):
            if not root:
                return 0
            
            l = pre_order(root.left)
            r = pre_order(root.right)
            self.maxi = max(self.maxi, l+r+root.val, root.val, l+root.val, r+root.val)
            
            return max(max(l,r) + root.val, root.val)
            
        pre_order(root)
        
        return self.maxi
        