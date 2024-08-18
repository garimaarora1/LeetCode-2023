class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder_traversal(root, remaining):
            if not root:
                return None

            left_result = inorder_traversal(root.left, remaining)
            if left_result is not None:
                return left_result
            remaining[0] -= 1
            if remaining[0] == 0:
                return root.val

            return inorder_traversal(root.right, remaining)
        remaining = [k]
        return inorder_traversal(root, remaining)
