class Solution:
    def bfs(self,node,rooms):
        queue = deque([node])
        visited = set([node])

        while queue:
            node = queue.popleft()

            for i in rooms[node]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return visited

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        ans = self.bfs(0,rooms)
        if len(ans) == len(rooms):
            return True
        return False