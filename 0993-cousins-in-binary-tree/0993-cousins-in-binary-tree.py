# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([root])
        
        while queue:
            n = len(queue)
                            
            sibling = False
            cousin = False

            for _ in range(n):
                
                node = queue.popleft()
                
                if not node:
                    sibling = False
                
                else:
                    if node.val == x or node.val == y:
                        if not cousin:
                            cousin, sibling = True, True
                        else:
                            return not sibling
                    
                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)
                    
                    queue.append(None)
            if cousin:
                return False
        return False
        
                    
                    