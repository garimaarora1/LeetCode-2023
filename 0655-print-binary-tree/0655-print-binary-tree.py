# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        """
        row = height
        cols = 2 ** height - 1
        """
        def get_height(root):
            if not root:
                return 0
            lh = get_height(root.left)
            rh = get_height(root.right)
            return max(lh, rh) + 1
        
        def dfs(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            tree[row][mid] = str(node.val)
            dfs(node.left, row+1, left, mid-1)
            dfs(node.right, row+1, mid+1, right)
        
        
        height = get_height(root)
        width = (2 ** height) - 1
        tree = [[''] * width for _ in range(height)]
        dfs(root, 0, 0, width-1)
        return tree