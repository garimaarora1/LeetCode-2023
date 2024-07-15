# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = True

    def binaryTreeHeight(self, root):
        if not root:
            return 0
        
        lh = self.binaryTreeHeight(root.left)
        rh = self.binaryTreeHeight(root.right)
        
        if abs(lh-rh) > 1:
            self.ans = False
            return 0
        
        return max(lh, rh) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.binaryTreeHeight(root)
        return self.ans
        

        
        
        
        
        