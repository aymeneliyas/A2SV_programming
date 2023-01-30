class Solution:
    def maxArea(self, height: List[int]) -> int:
        """

        """
        length = len(height)
        left = 0
        right = length-1
        ans = 0
        while left < right:
            minimum = min(height[left],height[right])
            area = minimum * (right-left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            ans = max(ans,area)
        return ans
