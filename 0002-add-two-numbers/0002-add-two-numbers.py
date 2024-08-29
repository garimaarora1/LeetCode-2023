# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        l3 = ListNode()
        head = l3
        while l1 or l2 or carry:
            curr_sum = carry
            
            if l1:
                curr_sum += l1.val
                l1 = l1.next

            if l2:
                curr_sum += l2.val
                l2 = l2.next
            
            carry = curr_sum // 10
            
            l3.next = ListNode(curr_sum % 10)
            l3 = l3.next
        return head.next