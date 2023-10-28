# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        def deleteChildren(root, value):
            if root is None:
                return None

            if root.val == value:
                if root.left:
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
                return None

            root.left = deleteChildren(root.left, value)
            root.right = deleteChildren(root.right, value)

            return root
        
        for val in to_delete:
            deleteChildren(root,val)
            for node in ans:
                if node.val == val:
                    ans = list(filter(lambda x: x.val != val, ans))
                deleteChildren(node,val)
        if root.val not in to_delete:
            ans.append(root)

        return set(ans)