class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(graph, start):
            distances = {node: float('inf') for node in range(1,n+1)}
            distances[start] = 0
            visited = set() 
            priority_queue = [(0, start)]
            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                if current_node in visited:
                    continue
                visited.add(current_node)

                for neighbor, weight in graph[current_node]:
                    
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
            return distances 
        
        
        graph = defaultdict(list)
        for source,target,time in times:
            graph[source].append([target,time])
        arr = dijkstra(graph,k)
        for key,val in arr.items():
            if val == float('inf'):
                return -1
        return max(arr.values())