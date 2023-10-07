class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def rec(i,j):
            if i == len(nums1) or j == len(nums2):
                return 0
            
            if nums1[i] == nums2[j]:
                return 1 + rec(i+1,j+1)
            else:
                return max(rec(i+1,j),rec(i,j+1))
            
        return rec(0,0)