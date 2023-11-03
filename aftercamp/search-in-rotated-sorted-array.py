class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        left = left%len(nums)
        right = len(nums)+left
        
        while left <= right:
            middle = left + (right - left)//2
            midIndex = middle%len(nums)
            if nums[midIndex] > target:
                right = middle-1
            else:
                if nums[midIndex] == target:
                    return midIndex
                left = middle+1
                   
        if nums[left % len(nums)] == target:
            return left % len(nums)
        return -1