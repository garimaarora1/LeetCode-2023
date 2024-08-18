# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        
        queue.append((root, 1))
        
        max_width = 1
        
        while queue:
            n = len(queue)
            level_res = []
            for i in range(n):
                node, node_idx = queue.popleft()
                if i == 0 or i == n-1:
                    level_res.append(node_idx)
                if node.left:
                    queue.append((node.left, node_idx * 2 + 0))
                    
                if node.right:
                    queue.append((node.right, node_idx * 2 + 1))
            if len(level_res) >= 2:
                curr_width = level_res[1] - level_res[0] + 1
                max_width = max(max_width, curr_width)
        return max_width
            
                
                
                
        