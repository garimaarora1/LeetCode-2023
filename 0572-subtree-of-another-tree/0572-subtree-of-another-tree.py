# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # traverse the sub tree and if the node value matches check if subtrees are identical
        if subRoot == None:
            return True
        if root == None:
            return False
        if root.val == subRoot.val:
            if self.is_identical(root, subRoot):
                return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
            
    def is_identical(self, root, subRoot):
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        if root.val == subRoot.val:
            return (self.is_identical(root.left, subRoot.left) and self.is_identical(root.right, subRoot.right))
        return False
            

            
        