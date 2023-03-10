# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkRight(self,root,depth,dic):
        if not root:
            return
        if depth not in dic:
            dic[depth] = root.val
        
        self.checkRight(root.right,depth+1,dic)
        self.checkRight(root.left,depth+1,dic)
        return

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}
        result = []
        self.checkRight(root,0,dic)
        
        for key,val in dic.items():
            result.append(val)
        return result