# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def _build_tree(left, right):
            if left > right:
                return
            nonlocal postorder_idx
            root_val = postorder[postorder_idx]
            postorder_idx -= 1
            
            root = TreeNode(root_val)
            
            root.right = _build_tree(inorder_map[root_val]+1, right)
            root.left = _build_tree(left, inorder_map[root_val]-1)
            
            return root

            
        left, right = 0, len(inorder) - 1
        postorder_idx = len(inorder) - 1
        
        inorder_map = dict()
        
        for i, val in enumerate(inorder):
            inorder_map[val] = i
            
        root = _build_tree(left, right)
        
        return root
        