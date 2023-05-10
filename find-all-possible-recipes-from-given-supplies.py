class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        edges = defaultdict(int)
        for idx,food in enumerate(recipes):
            for i in ingredients[idx]:
                graph[i].append(food)
            edges[food] = len(ingredients[idx])
        print(graph)

        def bfs(queue):
            ans = []
            while queue:
                node = queue.popleft()
                if node in recipes:
                    ans.append(node)
                
                for ver in graph[node]:
                    edges[ver] -= 1
                    if edges[ver] == 0:
                        queue.append(ver)

            return ans
        
        queue = deque()
        for i in supplies:
            if i in graph and i not in edges:
                queue.append(i)

        return bfs(queue)