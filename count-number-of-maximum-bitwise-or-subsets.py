class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = []
        maxp = 0
        for i in nums:
            maxp |= i
        for i in range(1,2 ** len(nums)):
            arr = []
            index = 0
            while i:
                if i & 1:
                    arr.append(nums[index])
                index += 1
                i >>= 1
            ans.append(arr)
        count = 0
        for i in ans:
            ans = 0
            for j in range(len(i)):
                ans |= i[j]
            if ans == maxp:
                count += 1
        return count