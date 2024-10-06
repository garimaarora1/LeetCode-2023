# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        curr = head
        
        # calculate LL length
        n = 1 # important
        while curr.next:
            n += 1
            curr = curr.next
        
        # close the ring
        curr.next = head
        
        k = k % n
        
        # find new tail and new head 
        new_tail = head
        for _ in range(n-k-1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
        