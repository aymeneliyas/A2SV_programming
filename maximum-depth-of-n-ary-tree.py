"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.ans = 0

    def maxDepth(self, root: 'Node') -> int:
        def dfs(root,depth):
            if not root:
                return 

            if not root.children:
                self.ans = max(depth+1, self.ans)
                return 
            
            for children in root.children:
                dfs(children,depth+1)
                
        dfs(root,0)
        return self.ans