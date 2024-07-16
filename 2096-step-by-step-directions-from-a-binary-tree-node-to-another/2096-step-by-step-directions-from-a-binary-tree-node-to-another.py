# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_path(self, root, value, path):
        if not root:
            return None
        if root.val == value:
            return True
            
        path.append("L")
        if self.find_path(root.left, value, path):
            return True
        path.pop()
        
        path.append("R")
        if self.find_path(root.right, value, path):
            return True
        path.pop()
        
        return False

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        shortest_path = []
        start_path, dest_path = [], []
        self.find_path(root, startValue, start_path)
        self.find_path(root, destValue, dest_path)
        
        common_path_len = 0
        
        while common_path_len < len(start_path) and common_path_len < len(dest_path) and start_path[common_path_len] == dest_path[common_path_len]:
            common_path_len += 1
            
        
        shortest_path.extend(["U" * (len(start_path)-common_path_len)])
        
        shortest_path.extend(dest_path[common_path_len:])
        
        return ''.join(shortest_path);
