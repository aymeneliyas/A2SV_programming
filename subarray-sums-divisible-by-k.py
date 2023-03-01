class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        arr = [0] * k
        arr[0] = 1
        tot = 0
        ans = 0
        for i in nums:
            tot += i
            ans += arr[tot%k]
            arr[tot%k] += 1
        return ans