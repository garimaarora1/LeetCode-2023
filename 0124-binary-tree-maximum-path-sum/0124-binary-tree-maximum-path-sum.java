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
    private int maxi;
    public int helperMaxPathSum(TreeNode root) {
        if(root == null) return 0;

        int left = Math.max(0, helperMaxPathSum(root.left));
        int right = Math.max(0, helperMaxPathSum(root.right));
        maxi = Math.max(maxi, left + right + root.val);

        return Math.max(left, right) + root.val;
    }

    public int maxPathSum(TreeNode root) {
        maxi = Integer.MIN_VALUE;
        helperMaxPathSum(root);
        return maxi;
    }
}