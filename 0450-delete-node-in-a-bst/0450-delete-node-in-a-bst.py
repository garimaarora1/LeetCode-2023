# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_in_order_successor(self, root):
        while root.left != None:
            root = root.left
        return root
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # case 1
            if root.left == None and root.right == None:
                return None
            # case 2
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            # case 3
            in_order_successor = self.get_in_order_successor(root.right)
            root.val = in_order_successor.val
            root.right = self.deleteNode(root.right, in_order_successor.val)
        return root