# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        # height of binary tree 
        
        def height(root):
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            return max(l, r) + 1
        
        def populate_res(root, low, high, row):
            if not root:
                return
            mid = (low + high) // 2
            res[row][mid] = str(root.val)
            populate_res(root.left, low, mid-1, row+1)
            populate_res(root.right, mid+1, high, row+1)
            
            
        
        
        row = height(root)
        cols = (2 **row) - 1
        res = [[""] * cols for _ in range(row)]
        
        populate_res(root, 0, cols, 0)
        return res
        
        
        