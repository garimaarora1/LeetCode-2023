# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
            
        curr = head
        
        prev = None
        
        K = k
        while curr and K != 0:
            K -= 1
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head.next = self.reverseKGroup(curr, k)
        
        return prev
            
        
        
        

            
        