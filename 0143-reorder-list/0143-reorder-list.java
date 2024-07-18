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
    public ListNode reverseLinkedList(ListNode head) {
        if (head == null || head.next == null) return head;
        
        ListNode prev = reverseLinkedList(head.next);
        head.next.next = head;
        head.next = null;
        return prev;
    }
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        ListNode fast = head;
        ListNode slow = head;
        
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        ListNode head2 = reverseLinkedList(slow.next);
        slow.next = null;
        ListNode head1 = head;
        ListNode tempNode;
        while (head2 != null) {
            tempNode = head1.next;
            head1.next = head2;
            head1 = head2;
            head2 = tempNode;
            
        }
        
        
        
    }
}