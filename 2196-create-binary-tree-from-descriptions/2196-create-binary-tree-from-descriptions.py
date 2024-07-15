# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        nodes_map = defaultdict(TreeNode)
        children = set()
        for parent, child, is_left in descriptions:
            
            children.add(child)
            if parent not in nodes_map:
                nodes_map[parent] = TreeNode(parent)
            if child not in nodes_map:
                nodes_map[child] = TreeNode(child)
            if is_left:
                nodes_map[parent].left = nodes_map[child]
            else:
                nodes_map[parent].right = nodes_map[child]

        for key in nodes_map.keys():
            if key not in children:
                return nodes_map[key]