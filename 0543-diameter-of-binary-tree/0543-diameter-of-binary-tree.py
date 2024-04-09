# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diam = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def find(root):
            if not root:
                return 0

            l = find(root.left)
            r = find(root.right)
            self.max_diam = max(self.max_diam, l+r)
            return max(l,r) + 1
        find(root)
        return self.max_diam