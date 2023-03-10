# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def level(self,root,dic,depth):
        if not root:
            return
        dic[depth].append(root.val)
        self.level(root.left,dic,depth+1)
        self.level(root.right,dic,depth+1)

        return
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        self.level(root,dic,0)
        result = []
        for key,val in dic.items():
            result.append(val)
        return result