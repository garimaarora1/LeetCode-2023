# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        
        right_side_view = []
        
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i == n-1:
                    right_side_view.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return right_side_view
                
                
                