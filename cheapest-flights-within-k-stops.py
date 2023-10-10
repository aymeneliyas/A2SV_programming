class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def dijkstra(graph, start):
            distances = [inf] * n
            distances[start] = 0
            
            priority_queue = deque([(0, start)])
            count = 0
            for i in range(k+1):
                size = len(priority_queue)
                for i in range(size):
                    current_distance, current_node = priority_queue.popleft()

                    for neighbor, weight in graph[current_node]:
                        
                        distance = current_distance + weight
                        if distance < distances[neighbor]:
                            distances[neighbor] = distance
                            priority_queue.append((distance, neighbor))
            return distances 
        
        
        graph = defaultdict(list)
        for fr,to,price in flights:
            graph[fr].append([to,price])
        
        distances = dijkstra(graph,src)
        if distances[dst] == inf:
            return -1
        
        return distances[dst]