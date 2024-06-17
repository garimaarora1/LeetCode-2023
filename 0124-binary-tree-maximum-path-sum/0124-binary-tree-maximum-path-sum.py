# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            l = max(0, dfs(root.left))
            r = max(0, dfs(root.right))
            self.maxi = max(self.maxi, l + r + root.val)
            return max(l,r) + root.val
    
        dfs(root)
        return self.maxi
        