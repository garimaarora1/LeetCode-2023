class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder_traversal(root):
            nonlocal k
            if not root:
                return None

            left_result = inorder_traversal(root.left)
            if left_result is not None:
                return left_result
            k -= 1
            if k == 0:
                return root.val

            return inorder_traversal(root.right)
        return inorder_traversal(root)
