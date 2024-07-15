# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# find the count of nodes greater than or equal to the root node value 
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def pre_order_traversal(root, max_so_far):
            if not root:
                return
            nonlocal count
            
            if root.val >= max_so_far:
                count += 1
            pre_order_traversal(root.left, max(max_so_far, root.val))
            pre_order_traversal(root.right, max(max_so_far, root.val))
                    
        count = 0
        pre_order_traversal(root, float('-inf'))
        return count