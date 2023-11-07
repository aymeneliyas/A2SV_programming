# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def rec(root):
            nonlocal ans
            if not root:
                return 
            if root.val >= low and root.val <= high:
                print(root.val)
                ans += root.val
            rec(root.left)
            rec(root.right)


            return ans
        
        return rec(root)