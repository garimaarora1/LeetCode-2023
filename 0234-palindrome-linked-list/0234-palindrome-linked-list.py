# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self, head):
        if not head or not head.next:
            return head
        prev = self.rev(head.next)
        head.next.next = head
        head.next = None
        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return True
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = self.rev(slow)
        
        fast = head
        while slow and fast:
            if slow.val != fast.val:
                return False
            fast = fast.next
            slow = slow.next
        return True