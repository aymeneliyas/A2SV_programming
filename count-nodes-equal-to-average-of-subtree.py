# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def getCount(self,root):
        if not root.left and not root.right:
            self.count += 1
            return [root.val,1]
        ans = None

        if not root.right or not root.left:
            if not root.right:
                ans = self.getCount(root.left)
            if not root.left:
                ans = self.getCount(root.right)
            total = root.val+ans[0]
            num = ans[1]+1
            if root.val == total//num:
                self.count += 1
            return [total , num]

        else:
            ans1 = self.getCount(root.left)
            ans2 = self.getCount(root.right)
            total = ans1[0] + ans2[0] + root.val
            count = ans1[1] + ans2[1] + 1
            if root.val == total//count:
                self.count += 1

            return [total,count]
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.getCount(root)
        return self.count