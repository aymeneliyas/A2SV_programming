class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        [3,1,2,4]
        e
        
        """
        index = 0
        for key,elm in enumerate(nums):
            if elm % 2 == 0:
                nums.insert(index,elm)
                nums.pop(key+1)
                index += 1
        return nums
