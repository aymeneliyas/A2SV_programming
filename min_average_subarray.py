class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[0:k]) / k
        tot = sum(nums[0:k])
        left = 0
        right = k
        while right < len(nums):
            tot -= nums[left]
            tot += nums[right]

            avg = tot / k
            ans = max(ans,avg)
            right += 1
            left += 1
        return ans
