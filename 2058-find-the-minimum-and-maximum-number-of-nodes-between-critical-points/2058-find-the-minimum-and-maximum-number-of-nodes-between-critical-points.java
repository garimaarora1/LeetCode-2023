/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        ListNode prev = head;
        ListNode node = head.next;
        int prev_index = -1;
        int first_index = -1;
        int minimum = Integer.MAX_VALUE;
        int maximum = Integer.MIN_VALUE;
        int criticalPoints = 0;
        int curr_index = 0;
        int[] res = {-1, -1};
        while (node != null && node.next != null) {
            curr_index ++;
            if ((prev.val > node.val && node.val < node.next.val) || (prev.val < node.val && node.val > node.next.val)) {
                criticalPoints ++;
                if (first_index == -1) {
                    first_index = curr_index;
                } else {
                    minimum = Math.min(minimum, curr_index-prev_index);
                    maximum = Math.max(maximum, curr_index-first_index);
                }
                prev_index = curr_index;
            }
            prev = node;
            node = node.next;
        }
        if (minimum != Integer.MAX_VALUE) {
            res[0] = minimum;
            res[1] = maximum;
       
        }
         return res;  
    }
}