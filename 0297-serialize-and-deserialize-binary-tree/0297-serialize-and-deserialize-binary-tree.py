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
        res = []
        def dfs_pre_order(root):
            if not root:
                res.append('N')
                return 
            res.append(str(root.val))
            dfs_pre_order(root.left)
            dfs_pre_order(root.right)
        dfs_pre_order(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def dfs_pre_order():
            nonlocal i
            i += 1
            if data[i] == 'N':
                return
            root = TreeNode(data[i])
            root.left = dfs_pre_order()
            root.right = dfs_pre_order()
            return root
            
        i = -1
        print(data)
        data = data.split(',')
        return dfs_pre_order()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))