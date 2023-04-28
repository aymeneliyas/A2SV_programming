class Solution:
    def bfs(self,target,deadends):
        visited = set(deadends)
        queue = deque([[0,0,0,0]])
        ans = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                val = ""
                for idx in node:
                    val += str(idx)
                print(val)
                if val == target:
                    return ans
                moves = self.possible(node)
                for move in moves:
                    print(val)
                    val = ""
                    for idx in move:
                        val += str(idx)
                    if val not in visited:
                        queue.append(move)
                        visited.add(val)
            ans += 1
        return -1

    def possible(self,lock):
        result = []
        for i in range(4):
            lock[i] += 1
            lock[i] %= 10
            result.append(lock[:])

            lock[i] -= 2
            lock[i] %= 10
            result.append(lock[:])

            lock[i] += 1
            lock[i] %= 10
        return result

    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1 
        return self.bfs(target,deadends)
        return 0