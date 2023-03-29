# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def fun(head):
            if head == None or head.next == None:
                return head
            h = head.next.next
            head, head.next = head.next, head
            
            next_node = fun(h)
            head.next.next = next_node
            return head
        
        return fun(head)