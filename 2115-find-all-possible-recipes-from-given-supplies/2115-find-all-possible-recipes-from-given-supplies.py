class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        inDegrees = {nodo: 0 for nodo in recipes + list(chain(*ingredients))}
        graph = defaultdict(set)
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].add(recipe)
                inDegrees[recipe] += 1
        queue = deque([node for node in inDegrees if inDegrees[node] == 0 and node in supplies])
        ans = []
        while queue:
            curNode = queue.popleft()
            if curNode in recipes:
                ans.append(curNode)
            for node in graph[curNode]:
                inDegrees[node] -= 1
                if inDegrees[node] == 0:
                    queue.append(node)
        return ans