# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        answer = [0]* len(values)
        stack = []
        for i, val in enumerate(values):
            while stack and values[stack[-1]] < val:
                smaller = stack.pop()
                answer[smaller] = val
            stack.append(i)
        return answer