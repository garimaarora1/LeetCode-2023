class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        '''
        1. Create adj list
        2. Initialize count_pairs, remaining_nodes, curr_component_size, visited
        3. BFS
        4. remaining_nodes -= curr_component_size
        5. count_pairs = curr_component_size * remaining_nodes
        '''
        
        # create adj list
        
        adj_list = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
            
        # intialize vars
        count_pairs = 0
        remaining_nodes = n
        visited = set()
        curr_component_size = 0
        
        # bfs
        def bfs(node):
            queue = deque()
            size = 1
            queue.append(node)
            visited.add(node)
            while queue:
                node = queue.popleft()
                for adj in adj_list[node]:
                    if adj not in visited:
                        size += 1
                        queue.append(adj)
                        visited.add(adj)
            return size
        
        # iteraring all nodes
        for i in range(n):
            if i not in visited:
                curr_component_size = bfs(i)
                remaining_nodes -= curr_component_size
                count_pairs += curr_component_size * (remaining_nodes)
        return count_pairs
            
