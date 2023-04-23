# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self,root,parent,grandParent):
        node = 0
        if not root:
            return 0
        if grandParent % 2 == 0:
            node = root.val
        return self.helper(root.left,root.val,parent) + self.helper(root.right,root.val,parent) + node

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.helper(root,3,3)