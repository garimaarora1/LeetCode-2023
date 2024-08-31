# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        parents = defaultdict(TreeNode)

        def dfs(root):
            
            if root.left:
                parents[root.left.val] = root
                dfs(root.left)
            
            if root.right:
                parents[root.right.val] = root
                dfs(root.right)
        
        dfs(root)
        
        queue = deque()
        queue.append(target)
        visited = set()
        while queue and k != 0:
            k -= 1
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                visited.add(node.val)

                if node.left and node.left.val not in visited:
                    queue.append(node.left)
                    
                if node.right and node.right.val not in visited:
                    queue.append(node.right)
                    
                if node.val in parents and parents[node.val].val not in visited:
                    queue.append(parents[node.val])
        
        res = []
        while queue:
            node = queue.popleft()
            res.append(node.val)
        return res
                
        