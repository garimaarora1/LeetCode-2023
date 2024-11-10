from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Dictionaries to store subtree heights and the max heights per tree level
        max_height_at_level = {}          # Highest subtree height at each level
        second_max_height_at_level = {}    # Second highest subtree height at each level
        subtree_heights = {}               # Height of each subtree rooted at each node
        node_level = {}                    # Level of each node in the tree

        def traverse(node: Optional[TreeNode], level: int = 0) -> int:
            if node is None:
                return 0
            
            # Traverse left and right subtrees to get their heights
            left_subtree_height = traverse(node.left, level + 1)
            right_subtree_height = traverse(node.right, level + 1)
            
            # Calculate the current node's subtree height
            curr_subtree_height = 1 + max(left_subtree_height, right_subtree_height)
            subtree_heights[node.val] = curr_subtree_height
            node_level[node.val] = level
            
            # Update largest and second-largest heights at the current level
            if curr_subtree_height > max_height_at_level.get(level, 0):
                second_max_height_at_level[level] = max_height_at_level.get(level, 0)
                max_height_at_level[level] = curr_subtree_height
            elif curr_subtree_height > second_max_height_at_level.get(level, 0):
                second_max_height_at_level[level] = curr_subtree_height

            return curr_subtree_height

        # Perform initial DFS traversal to fill in subtree heights and level heights
        traverse(root, 0)

        # Process each query by removing the subtree and calculating the new tree height
        result = []
        for query_node in queries:
            level = node_level[query_node]
            
            # Determine max height after subtree removal
            if subtree_heights[query_node] == max_height_at_level[level]:
                new_height = level + second_max_height_at_level[level] - 1
            else:
                new_height = level + max_height_at_level[level] - 1
            
            result.append(new_height)
        
        return result
