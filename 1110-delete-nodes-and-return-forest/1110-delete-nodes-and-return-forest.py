# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root:
                return None
            
            is_deleted = root.val in to_delete_set
            
            if is_root and not is_deleted:
                res.append(root)
            
            root.left = helper(root.left, is_deleted)
            root.right = helper(root.right, is_deleted)
            
            return None if is_deleted else root
                
                
        helper(root, True)
        return res
