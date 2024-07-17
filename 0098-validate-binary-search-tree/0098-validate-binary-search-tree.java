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
    public boolean helperIsValidBST(TreeNode root, Integer mini, Integer maxi) {
        if(root == null) return true;

        if (mini != null && root.val <= mini) return false;

        if (maxi != null && root.val >= maxi) return false;

        return helperIsValidBST(root.left, mini, root.val) && helperIsValidBST(root.right, root.val, maxi);

    }
    public boolean isValidBST(TreeNode root) {

        return helperIsValidBST(root, null, null);
        
    }
}