# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.res = []
        self.i = -1

    def dfs(self, node):
        if not node:
            self.res.append("N")
            # important
            return
        # important
        self.res.append(str(node.val))
        self.dfs(node.left)
        self.dfs(node.right)

    def build_tree(self, values):
        self.i += 1
        if values[self.i] == 'N':
            return None
        
        node = TreeNode(values[self.i])
        node.left = self.build_tree(values)
        node.right = self.build_tree(values)
        return node

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.dfs(root)
        print(self.res)
        return ','.join(self.res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(',')
        root = self.build_tree(values)
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))