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
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> heap = new PriorityQueue<>((a, b) -> a.val - b.val);
        for(ListNode list : lists) {
            if(list != null) heap.add(list);
        }
        
        ListNode dummyNode = new ListNode();
        ListNode head = dummyNode;
        
        while(!heap.isEmpty()) {
            ListNode node = heap.poll();
            dummyNode.next = node;
            dummyNode = dummyNode.next;
            
            if(node.next != null){ 
                heap.add(node.next);
            }
        }
        return head.next;
        
    }
}