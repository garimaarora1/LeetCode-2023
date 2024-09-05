class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
         # Check if there are at least k nodes left in the list
        cursor = head
        for _ in range(k):
            if not cursor:
                return head
            cursor = cursor.next
        
        # Reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # head is now the last node in the reversed segment
        # Connect it to the result of the next reverseKGroup call
        head.next = self.reverseKGroup(curr, k)
        
        # prev is the new head of the reversed segment
        return prev