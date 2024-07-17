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
    private int preOrderIdx;
    private Map<Integer, Integer> inorderMap;
    
    public TreeNode helperBuildTree(int left, int right, int[] preorder) {
        if (left > right) return null;

        int rootVal = preorder[preOrderIdx];
        preOrderIdx ++;

        TreeNode root = new TreeNode(rootVal);
        int inorderIdx = inorderMap.get(rootVal);
        root.left = helperBuildTree(left, inorderIdx-1, preorder);
        root.right = helperBuildTree(inorderIdx+1, right, preorder);
        return root;
    }
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        preOrderIdx = 0;
        int left = 0;
        int right = preorder.length - 1;
        inorderMap = new HashMap<>();

        for(int i = 0; i<inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }

        return helperBuildTree(left, right, preorder);
    }
}