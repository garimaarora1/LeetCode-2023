# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

Approach:

Take the first node of each of the linked lists
and add it into a heap. When you add it to the heap
add (node.val, i) where i is the ith list.

Create a dummy node head.

Pop the first node from the heap and make it the
next node in the dummy-list. Remember to add the
first node from the ith linked list into the heap
since we just removed a node from this list from the heap.

Repeat until the heap is empty.

https://leetcode.com/problems/merge-k-sorted-lists/discuss/1032502/Python-Simple-Heap-Solution
"""
class Solution:
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        return head.next
        