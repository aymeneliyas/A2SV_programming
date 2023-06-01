class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def solve(index,arr,memo):
            if index >= len(arr):
                return 0
            if index == len(arr) -1:
                return arr[index]
            
            if index in memo:
                return memo[index]
            
            memo[index] = max(solve(index+1,arr,memo),solve(index+2,arr,memo)+arr[index])
            return memo[index]
        

        return max(solve(0,nums[1:],{}) , solve(0,nums[:len(nums)-1],{}))