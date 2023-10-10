class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def rec(index,flag):
            if index == len(nums1):
                return 0
        
            if nums1[index] > nums1[index-1] and nums2[index] > nums2[index-1]:
                val2 = rec(index+1,False)
                val1 = inf
                if nums1[index] > nums2[index-1] and nums1[index-1] < nums2[index]:
                    nums1[index],nums2[index] = nums2[index],nums1[index]    
                    val1 = 1 +rec(index+1,True)
                    nums1[index],nums2[index] = nums2[index],nums1[index]
                
                return min(val1,val2)

            nums1[index],nums2[index] = nums2[index],nums1[index]
            ans1 = 1 + rec(index+1,True)
            nums1[index],nums2[index] = nums2[index],nums1[index]
            
            return ans1



        ans1= rec(1,False)
        nums1[0],nums2[0]=nums2[0],nums1[0]
        ans2=rec(1,True)+1

        return min(ans1,ans2)