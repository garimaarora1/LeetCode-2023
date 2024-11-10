class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        perfect_subtree_sizes = []

        def dfs(root):
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            if left_height == right_height and left_height >= 0:
                perfect_subtree_sizes.append(2 ** (left_height + 1) - 1)  # Store number of nodes, not height
                return left_height + 1  # Height of perfect subtree
            return -1

        dfs(root)

        # Return the k-th largest perfect subtree size
        if k <= len(perfect_subtree_sizes):
            return sorted(perfect_subtree_sizes)[-k]  # Return k-th largest
        return -1
