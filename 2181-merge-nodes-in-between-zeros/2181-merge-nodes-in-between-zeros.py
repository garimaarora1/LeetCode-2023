# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1=ListNode(-1)
        ans=head1
        temp=head.next
        s=0
        while temp:
            if temp.val!=0:
                s+=temp.val
            else:
                head1.next=ListNode(s)
                head1=head1.next
                s=0
            temp=temp.next
        return ans.next