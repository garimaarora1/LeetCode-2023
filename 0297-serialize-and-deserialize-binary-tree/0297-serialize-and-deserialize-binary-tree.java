/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {
    StringBuilder res;
    int i;
    public String dfs(TreeNode root, String res) {
        if (root == null) {
            res += "N,";
        } else {
        res += res.valueOf(root.val) + ",";
        res = dfs(root.left, res);
        res = dfs(root.right, res);
        }
        return res;
    }

    public TreeNode buildTree(List<String> l) {
    // Recursive deserialization.
    if (l.get(0).equals("N")) {
      l.remove(0);
      return null;
    }

    TreeNode root = new TreeNode(Integer.valueOf(l.get(0)));
    l.remove(0);
    root.left = buildTree(l);
    root.right = buildTree(l);

    return root;
        
    }
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        return dfs(root, "");
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] values = data.split(",");
        List<String> data_list = new LinkedList<String>(Arrays.asList(values));
        i = -1;
        return buildTree(data_list);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));