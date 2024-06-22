"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        clone_graph = {}
        queue = deque()
        queue.append(node)
        clone_graph[node] = Node(node.val)
        while queue:
            n = queue.popleft()
            for adj in n.neighbors:
                if adj not in clone_graph:
                    queue.append(adj)
                    clone_graph[adj] = Node(adj.val)
                clone_graph[n].neighbors.append(clone_graph[adj])
        return clone_graph[node]