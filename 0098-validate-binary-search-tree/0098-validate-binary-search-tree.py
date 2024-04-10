# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkBST(self, root, mini, maxi):
        if not root:
            return True
        if mini != None and root.val <= mini:
            return False
        if maxi != None and root.val >= maxi:
            return False
        return self.checkBST(root.left, mini, root.val) and self.checkBST(root.right, root.val, maxi)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, None, None)
        
 