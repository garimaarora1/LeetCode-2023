# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self, node):
        if not node or not node.next:
            return node
        prev = self.rev(node.next)
        node.next.next = node
        node.next = None
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = self.rev(slow.next)
        slow.next = None

        
        # merge
        head1 = head
        
        while head2:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp
        
        
        