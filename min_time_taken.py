from typing import List


from typing import List

from collections import defaultdict,deque
class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list)
        incoming = [0] * (n+1)
        
        for x,y in edges:
            graph[x].append(y)
            incoming[y] += 1
            
        queue = deque()
        for idx,val in enumerate(incoming):
            if idx != 0 and val == 0:
                queue.append(idx)
        
        ans = [0] * (n+1)
        count = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                ans[node] = str(count)
                for ver in graph[node]:
                    incoming[ver] -= 1
                    if incoming[ver] == 0:
                        queue.append(ver)
            
            count += 1
        
        
        
        return " ".join(ans[1:])