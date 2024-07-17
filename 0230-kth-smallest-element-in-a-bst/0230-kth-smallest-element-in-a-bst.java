/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public ArrayList<Integer> inorder(TreeNode root, ArrayList<Integer> res) {
        if (root == null) return res;
        inorder(root.left, res);
        res.add(root.val);
        inorder(root.right, res);
        return res;
    }

    public int kthSmallest(TreeNode root, int k) {
        ArrayList<Integer> res = inorder(root, new ArrayList<Integer>());
        return res.get(k-1);
    }
}