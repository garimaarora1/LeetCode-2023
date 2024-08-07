# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, mini, maxi):
            # important
            if not root:
                return True
            # important to compare mini and maxi with None
            if mini != None and root.val <= mini:
                return False
            if maxi != None and root.val >= maxi:
                return False
            # impartant to return
            return dfs(root.left, mini, root.val) and dfs(root.right, root.val, maxi)
        # important to return
        return dfs(root, None, None)
    