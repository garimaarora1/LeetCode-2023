# from collections import deque

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # Initialize a queue for BFS
        queue = deque([root])
        root.val = 0  # As per the problem statement, the root's value should be set to 0
        
        while queue:
            level_size = len(queue)
            current_level_nodes = []
            next_level_sum = 0
            
            # First pass: collect nodes and calculate the level sum
            for _ in range(level_size):
                node = queue.popleft()
                current_level_nodes.append(node)
                
                if node.left:
                    next_level_sum += node.left.val
                    queue.append(node.left)
                if node.right:
                    next_level_sum += node.right.val
                    queue.append(node.right)
            
            # Second pass: update each node's value with the sum of its cousins
            for node in current_level_nodes:
                sum_of_cousins = next_level_sum
                
                if node.left:
                    sum_of_cousins -= node.left.val
                if node.right:
                    sum_of_cousins -= node.right.val
                
                if node.left:
                    node.left.val = sum_of_cousins
                if node.right:
                    node.right.val = sum_of_cousins
        
        return root
