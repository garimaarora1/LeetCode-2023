# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        
        c = ListNode()
        head = c
        while a and b:
            if a.val < b.val:
                c.next = a
                a = a.next
            else:
                c.next = b
                b = b.next
            c = c.next
        if a:
            c.next = a
        if b:
            c.next = b
        return head.next
                