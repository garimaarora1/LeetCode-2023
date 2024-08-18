# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = float('-inf')

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, curr_max, curr_min):
            if not root:
                return
            
            curr_max = max(curr_max, root.val)
            curr_min = min(curr_min, root.val)
            diff1 = abs(curr_max - root.val)
            diff2 = abs(curr_min - root.val)
            self.maxi = max(self.maxi, diff1, diff2)
            dfs(root.left, curr_max, curr_min)
            dfs(root.right, curr_max, curr_min)
            
        dfs(root, float('-inf'), float('inf'))
        
        return self.maxi
        
        