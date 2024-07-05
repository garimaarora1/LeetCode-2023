import sys
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        i=0
        prev = head.val 
        node = head.next 
        locs = []
        while node and node.next: 
            i += 1
            if prev < node.val > node.next.val or prev > node.val < node.next.val: locs.append(i)
            prev = node.val 
            node = node.next 
        if len(locs) < 2: return [-1, -1]
        return [min(locs[i] - locs[i-1] for i in range(1, len(locs))), locs[-1] - locs[0]]