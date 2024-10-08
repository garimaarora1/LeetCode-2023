class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        all_ingredients = set(chain(*ingredients))  # Flatten the ingredients
        all_nodes = set(recipes).union(all_ingredients) 
        in_degrees = {node: 0 for node in all_nodes}
        
        graph = defaultdict(set)

        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].add(recipe)
                in_degrees[recipe] += 1
        queue = deque([node for node in in_degrees if in_degrees[node] == 0 and node in supplies])
        ans = []

        while queue:
            curr = queue.popleft()
            if curr in recipes:
                ans.append(curr)
            for node in graph[curr]:
                in_degrees[node] -= 1
                if in_degrees[node] == 0:
                    queue.append(node)
        return ans