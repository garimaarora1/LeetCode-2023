# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                res.append("N")
                # important: return
                return
            # important: str
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        res = []
        dfs(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def dfs():
            self.i += 1
            if values[self.i] == 'N':
                return
            node = TreeNode(values[self.i])
            node.left = dfs()
            node.right = dfs()
            return node
        # important: self
        self.i = -1
        values = data.split(',')
        root = dfs()
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))