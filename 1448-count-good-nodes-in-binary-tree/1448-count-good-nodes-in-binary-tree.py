# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# find the count of nodes greater than or equal to the root node value 
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def pre_order(root, max_so_far):
            nonlocal c
            if max_so_far <= root.val:
                c += 1
            if root.left:
                pre_order(root.left, max(root.val, max_so_far))
            if root.right:
                pre_order(root.right, max(root.val, max_so_far))
        c = 0
        pre_order(root, float('-inf'))
        return c
        
        
        