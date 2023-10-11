# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dic = defaultdict(list)
        res = []
        def rec(root):
            if not root:
                return "null"

            val =  ",".join([str(root.val) , rec(root.left),rec(root.right)])
            if len(dic[val]) == 1:
              res.append(root)
            dic[val].append(root)
            return val
        rec(root)
        return res