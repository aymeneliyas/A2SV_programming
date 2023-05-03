# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        conn = collections.defaultdict(list)
        graph = defaultdict(list)

        def getgraph(parent,child):
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
            
            if child.left:
                getgraph(child,child.left)

            if child.right:
                getgraph(child,child.right)
            
        def dfs(k,arr):
            count = 0
            queue = deque([target.val])
            visited = set([target.val])
            print(queue)
            while queue:
                n = len(queue)
                for _ in range(n):
                    node = queue.popleft()
                    if k == 0:
                        arr.append(node)
                    for i in graph[node]:
                        if i not in visited:
                            queue.append(i)
                            visited.add(i)
                k -= 1
            return arr
        

        getgraph(None,root)
        arr = []

        return dfs(k,arr)