# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def rec(root,cursum,dic):
            nonlocal count
            if not root:
                return 0
            
            cursum += root.val
            if cursum - targetSum in dic:
                count += dic[cursum-targetSum]

            dic[cursum] += 1
            rec(root.left,cursum,dic)
            rec(root.right,cursum,dic)
            
            dic[cursum] -= 1
            cursum -= root.val
            
        dic = defaultdict(int)
        dic[0] = 1
        
        rec(root,0,dic)
        return count