# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def array_to_tree(left, right):
            if left > right:
                return
            nonlocal preorder_index
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            preorder_index += 1
            
            root.left = array_to_tree(left, inorder_map[root_val]-1)
            root.right = array_to_tree(inorder_map[root_val]+1,right)
            
            return root
            
        preorder_index = 0 
        inorder_map = {}
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx
        print(inorder_map)
        left, right = 0, len(inorder)-1
        root = array_to_tree(left, right)
        return root