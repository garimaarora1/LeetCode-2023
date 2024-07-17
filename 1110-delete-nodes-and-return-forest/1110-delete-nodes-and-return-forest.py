# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        to_delete_set = set(to_delete)    
        res = []

        def _delNodes(root, is_root):
            if not root:
                return
            is_deleted = root.val in to_delete_set
            
            if is_root and not is_deleted:
                res.append(root)    

            root.left = _delNodes(root.left, is_deleted)
            root.right = _delNodes(root.right, is_deleted)
                
            return None if is_deleted else root

        _delNodes(root, True)
        return res
        