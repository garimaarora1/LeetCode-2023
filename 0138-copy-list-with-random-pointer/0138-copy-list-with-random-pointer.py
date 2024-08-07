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
        # important
        # ll_dict = {None: None}
        if not head:
            return head
        ll_dict = {}

        curr = head
        
        while curr:
            ll_dict[curr] = Node(curr.val)
            curr = curr.next
        for curr, copy_node in ll_dict.items():
            if curr:
                if curr.next:
                    copy_node.next = ll_dict[curr.next]
                if curr.random:
                    copy_node.random = ll_dict[curr.random]
        return ll_dict[head]