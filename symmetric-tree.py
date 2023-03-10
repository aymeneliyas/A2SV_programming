# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self,root1,root2):
        if root1 and not root2:
            return False
        if root2 and not root1:
            return False
        if not root1 and not root2:
            return True
        if root1.val != root2.val:
            return False

        left = self.compare(root1.left,root2.right)
        right = self.compare(root1.right,root2.left)

        return left and right
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compare(root.left,root.right)