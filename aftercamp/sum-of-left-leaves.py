# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def rec(root):
            if not root:
                return 0
            if root.left and not root.left.left and not root.left.right:
               return root.left.val + rec(root.right)
            else:
                return rec(root.left )+ rec(root.right)
        return rec(root)
            
