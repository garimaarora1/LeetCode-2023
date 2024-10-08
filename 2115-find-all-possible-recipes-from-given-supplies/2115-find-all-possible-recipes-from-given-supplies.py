class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(set)
        numRecipes = len(recipes)
        in_degree = [0] * numRecipes
        queue = deque()
        res = []
        recipe_index = {recipe: i for i, recipe in enumerate(recipes)}  # Map recipe names to indices

        # Build graph and in-degree list
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].add(recipe)
                in_degree[recipe_index[recipe]] += 1

        # Initialize queue with supplies
        for supply in supplies:
            if supply in graph:
                queue.append(supply)

        # Process nodes in topological order
        while queue:
            cur_ingredient = queue.popleft()

            for recipe in graph[cur_ingredient]:
                idx = recipe_index[recipe]
                in_degree[idx] -= 1
                if in_degree[idx] == 0:
                    res.append(recipe)
                    queue.append(recipe)

        return res
