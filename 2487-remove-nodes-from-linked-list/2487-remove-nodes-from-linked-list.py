# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ms = []
        curr = ListNode()
        head1 = curr
        while head:
            while ms and head.val > ms[-1]:
                ms.pop()
            ms.append(head.val)
            head = head.next
        
        
        for i,item in enumerate(ms):
            curr.val = item
            if i != len(ms)-1:
                curr.next = ListNode()
                curr = curr.next
        curr = None
        return head1
        