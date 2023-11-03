class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        val = 0
        for i in range(3000):
            if i in arr:
                continue
            if val == k:
                return i
            val += 1
        