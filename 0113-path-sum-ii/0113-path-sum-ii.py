# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        
        def dfs(root, curr_path, curr_sum):
            if not root:
                return
            curr_path.append(root.val)
            curr_sum += root.val
            if not root.left and not root.right and curr_sum == targetSum:
                res.append(curr_path[:])

            dfs(root.left, curr_path, curr_sum)

            dfs(root.right, curr_path, curr_sum)

            curr_path.pop()
            
        dfs(root, [], 0)
        return res