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
    private int count;
    private int result;

    private void inorder(TreeNode root, int k) {
        if (root == null) return;
        
        inorder(root.left, k);
        
        count++;
        if (count == k) {
            result = root.val;
            return;
        }
        
        inorder(root.right, k);
    }

    public int kthSmallest(TreeNode root, int k) {
        count = 0;
        inorder(root, k);
        return result;
    }
}
