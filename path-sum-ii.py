# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return []
        def dfs(root,path):
            if not root.left and not root.right:
                path += [root.val]
                res.append(path)
                return
            if root.left:
                dfs(root.left,path+[root.val])
            if root.right:
                dfs(root.right,path+[root.val])
            return 
        ans = []        
        dfs(root,[])
        for arr in res:
            if sum(arr) == targetSum:
                ans.append(arr)
        return ans