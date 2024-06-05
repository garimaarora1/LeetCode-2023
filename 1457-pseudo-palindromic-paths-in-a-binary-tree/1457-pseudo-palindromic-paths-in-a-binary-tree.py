# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, freq_map):
            if not root:
                return 
            
            nonlocal count
            
            freq_map[root.val] += 1
            
            if not root.left and not root.right:
                odd_parity = sum(1 for val in freq_map.values() if val%2 != 0)
                if odd_parity <= 1:
                    count += 1
            dfs(root.left, freq_map)
            dfs(root.right, freq_map)
            
            freq_map[root.val] -= 1
        
        freq_map = defaultdict(int)
        count = 0
        dfs(root, freq_map)
        return count