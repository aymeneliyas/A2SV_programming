class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0 
        while idx < k:
            val = nums.pop()
            nums.insert(0,val)
            idx+=1
