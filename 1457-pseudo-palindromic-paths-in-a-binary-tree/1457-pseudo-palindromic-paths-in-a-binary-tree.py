# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # 1. Find all root to leaf paths: pre-order DFS traversal
        # 2. At the root node check that we should have at most one number with odd freq (maintain dictionary for this)
        # TODO: Can avoid using dict by using bit manipulation
        
        def dfs(node, freq):
            if not node:
                return
            nonlocal count
            freq[node.val] += 1
            
            if node.left == None and node.right == None:
                odd_count = sum(1 for val in freq.values() if val%2 == 1)
                if odd_count <=1:
                    count += 1
            dfs(node.left, freq)
            dfs(node.right, freq)
                    
            freq[node.val] -= 1
        
        count = 0
        freq = defaultdict(int)
        dfs(root, freq)
        return count
        