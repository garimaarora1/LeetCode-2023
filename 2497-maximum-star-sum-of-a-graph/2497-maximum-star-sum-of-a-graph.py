class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], K: int) -> int:
        if edges == []:
            return max(vals)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        max_sum = max(vals)

        for key, nodes in graph.items():
            # print(key, nodes)
            curr_sum = vals[key]
            values = []
            star_edge_values = []
            for node in nodes:
                values.append(vals[node])
            values.sort(reverse=True)
            for value in values[:K]:
                if value < 0:
                    break
                star_edge_values.append(value)
            curr_sum += sum(star_edge_values)
            max_sum = max(max_sum, curr_sum)
        return max_sum
            
        