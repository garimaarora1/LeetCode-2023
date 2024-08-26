# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or not head.next or k == 0:
            return head
        
        # close the LL into a ring
        curr = head
        n = 1 # important
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = head
        k = k % n
        
        # find new tail and new head
        new_tail = head
        for _ in range(n-k-1): # important
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head