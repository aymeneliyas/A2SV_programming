# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def rec(root):
            if not root or root.val == p.val or root.val == q.val:
                return root
            
            l = rec(root.left)
            r = rec(root.right)
            
            if not r:
                return l
            elif not l:
                return r
            else:
                return root

        return rec(root)