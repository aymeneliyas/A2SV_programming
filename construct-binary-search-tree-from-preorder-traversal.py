# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        for num in preorder:
            root = self.insert(root,num)
        return root

    def insert(self,root,val):
        if not root:
            return TreeNode(val,None,None)
        if root.val > val:
            root.left = self.insert(root.left,val)
        else:
            root.right = self.insert(root.right,val)
        return root