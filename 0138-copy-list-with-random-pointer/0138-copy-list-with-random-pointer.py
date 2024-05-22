"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copy = {None:None}
        curr = head
        while curr:
            original_to_copy[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = original_to_copy[curr]
            copy.next = original_to_copy[curr.next]
            copy.random = original_to_copy[curr.random]
            curr = curr.next
        return original_to_copy[head]