class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder_traversal(root):
            if not root:
                return None

            left_result = inorder_traversal(root.left)
            if left_result is not None:
                return left_result

            self.k -= 1
            if self.k == 0:
                return root.val

            return inorder_traversal(root.right)
        self.k = k
        return inorder_traversal(root)
