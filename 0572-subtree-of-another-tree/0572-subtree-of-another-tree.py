# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False
        if root1.val == root2.val: 
            return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not subRoot:
            return True
        if not root:
            return False
                                                                                
        if root.val == subRoot.val: 
            if self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            