# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sort(self,list1,list2):
        result = []
        left = 0
        right = 0
        size1 = len(list1)
        size2 = len(list2)
        while left < size1 and right < size2:
            if list1[left] < list2[right]:
                result.append(list1[left])
                left += 1
            
            else:
                result.append(list2[right])
                right += 1
            
        if right < size2:
            result.extend(list2[right:])
        if left < size1:
            result.extend(list1[left:])
        
        return result

    def mergeSorted(self,root):
        if not root:
            return []
        
        left = self.mergeSorted(root.left)
        right = self.mergeSorted(root.right)

        arr = self.sort(left[:],right[:])
        return self.sort(arr[:],[root.val])
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.mergeSorted(root)[k-1]