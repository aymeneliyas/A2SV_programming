# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # print(root1.val)
        if not (root1 or root2):
            return True
       
        if not (root1 and root2) or root1.val != root2.val:
            return False

        if (root1.left and root2.left) or (root1.right and root2.right):
            ans1 = self.flipEquiv(root1.right,root2.left)
            ans2 = self.flipEquiv(root1.left,root2.right)
            ans3 = self.flipEquiv(root1.left,root2.left)
            ans4 = self.flipEquiv(root1.right,root2.right)
            return (ans1 and ans2) or (ans3 and ans4)
        else:
            return self.flipEquiv(root1.right,root2.left) and self.flipEquiv(root1.left,root2.right)