# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkMode(self,root,dic):
        if not root:
            return
        dic[root.val] += 1
        self.checkMode(root.left,dic)
        self.checkMode(root.right,dic)
        return

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        self.checkMode(root,dic)
        result = []
        big = max(dic.values())
        for key,val in dic.items():
            if val == big:
                result.append(key)
        return result