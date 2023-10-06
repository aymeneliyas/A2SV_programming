class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        def dijkstra(graph, start):
            distances = {node: float('-inf') for node in range(n)}
            distances[start] = 0
            visited = set() 
            priority_queue = [(1, start)]
            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                if current_node in visited:
                    continue
                visited.add(current_node)

                for neighbor, weight in graph[current_node]:
                    distance = abs(current_distance) * weight
                    if distance > distances[neighbor]:
                        distances[neighbor] = abs(distance)
                    heapq.heappush(priority_queue, (-1 * distance, neighbor))
            return distances 
        

        graph = defaultdict(list)
        i = 0
        for start,end in edges:
            graph[start].append([end,succProb[i]])
            graph[end].append([start,succProb[i]])
            i += 1
        distances = dijkstra(graph,start_node)
        ans = distances[end_node]
        if ans == float('-inf'):
            return 0
        return ans