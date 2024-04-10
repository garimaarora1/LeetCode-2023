# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.mini = float('inf')
        value = root.val
        def pre_order(root):
            if not root:
                return 
            if root.val > value:
                self.mini = min(self.mini, root.val)
            pre_order(root.left)
            pre_order(root.right)
            
        pre_order(root)
        return -1 if self.mini == float('inf') else self.mini