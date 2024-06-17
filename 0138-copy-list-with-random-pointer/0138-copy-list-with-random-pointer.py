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
        ll_dict = {None: None}
        
        curr = head
        
        while curr:
            ll_dict[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy_node = ll_dict[curr]
            copy_node.next = ll_dict[curr.next]
            copy_node.random = ll_dict[curr.random]
            curr = curr.next
        return ll_dict[head]