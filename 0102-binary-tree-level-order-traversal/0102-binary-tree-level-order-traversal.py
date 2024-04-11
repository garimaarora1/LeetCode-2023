# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        q = [root]
        res = []
        while q:
            l = len(q)
            curr_level = []
            for i in range(l):
                ele = q.pop(0)
                curr_level.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            res.append(curr_level)
        return res
            
                
                
                
            
        
        