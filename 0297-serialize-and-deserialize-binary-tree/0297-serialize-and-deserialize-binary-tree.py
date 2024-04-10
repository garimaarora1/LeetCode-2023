# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
        
    def serialize(self, root):
        res = []
        def pre_order(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            pre_order(root.left)
            pre_order(root.right)
        pre_order(root)
        return ",".join(res)
        

    def deserialize(self, data):
        nodes = data.split(",")
        self.i = -1
        def build_tree():
            self.i += 1
            if nodes[self.i] == "N":
                return None
            new_node = TreeNode(int(nodes[self.i]))
            new_node.left = build_tree()
            new_node.right = build_tree()
            
            return new_node
        return build_tree()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))