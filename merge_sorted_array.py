class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums2_ptr = 0
        index = 0
        while nums2_ptr < n:
            if index > m-1+nums2_ptr:
                while index < m + n:
                    nums1[index] = nums2[nums2_ptr]
                    index+=1
                    nums2_ptr+=1
            
            elif nums1[index] > nums2[nums2_ptr]:
                
                k = m - index + nums2_ptr
    
                while k > 0:
                    nums1[index+k] = nums1[index+k-1]
                    k -= 1
            
                nums1[index] = nums2[nums2_ptr]
                nums2_ptr += 1
                index += 1
            else:
                index += 1
