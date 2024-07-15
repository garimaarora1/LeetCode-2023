# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        
        #inorder: elements are traversed in asc order
        def dfs(root):
            nonlocal res
            nonlocal k
            if not root:
                return
            dfs(root.left)
            k -= 1
            if k == 0:
                res = root.val
                return
            dfs(root.right)
        dfs(root)
        return res
                