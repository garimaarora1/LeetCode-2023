# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def goodNodes(self, root: TreeNode) -> int:
        
        def pre_order_traversal(root, max_seen_so_far):
            if not root:
                return 
            if root.val >= max_seen_so_far:
                self.count += 1
                max_seen_so_far = root.val
            
            pre_order_traversal(root.left, max_seen_so_far)
            pre_order_traversal(root.right, max_seen_so_far)
            
        
        pre_order_traversal(root, root.val)
        return self.count
        
        
        
        