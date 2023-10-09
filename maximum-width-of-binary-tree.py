# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = deque([[root,1]])

        while queue:
            size = len(queue)

            for i in range(size):
                node,index = queue.popleft()
                print(len(queue))
                if i == 0:
                    front = index
                if i == size-1:
                    last = index 
                if node.left:
                    queue.append([node.left,(2 * index) + 1])
                if node.right:
                    queue.append([node.right,(2 * index) + 2])
            ans = max(ans,(last-front)+1)
        
        return ans