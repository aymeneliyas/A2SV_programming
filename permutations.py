class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            result = []

            if len(nums) == 1:
                return [nums[:]]

            for i in range(len(nums)):
                n = nums.pop(0)
                arr = self.permute(nums)

                for val in arr:
                    val.append(n)

                result.extend(arr)
                nums.append(n)
            
            return result