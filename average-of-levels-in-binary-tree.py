# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self,root,ans):
        visited = set([root])
        queue = deque([root])

        while queue:
            n = len(queue)
            tot = 0
            for _ in range(n):
                node = queue.popleft()

                if node.left:
                    visited.add(node.left)
                    queue.append(node.left)
                if node.right:
                    visited.add(node.right)
                    queue.append(node.right)
                tot += node.val
            ans.append(tot/n)
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        self.bfs(root,ans)
        return ans