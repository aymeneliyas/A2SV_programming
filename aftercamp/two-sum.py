class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        dic = defaultdict(list)
        for key,val in enumerate(nums):
            dic[val].append(key)
        
        nums.sort()

        result = []
        while left < right:
            val = nums[left] + nums[right]
            if val == target:
                if nums[left] == nums[right]:
                    result.append(dic[nums[left]][0])
                    result.append(dic[nums[right]][1])
                else:
                    result.append(dic[nums[left]][0])
                    result.append(dic[nums[right]][0])
                    
                break
            
            elif val > target:
                right -= 1
            else:
                left += 1
        
        return result