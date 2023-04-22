class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(start, path):
            if len(path) > 1:
                    ans.append(path[:])
            visited = set() 
            
            for i in range(start, len(nums)):
                if nums[i] in visited:
                    continue
                if not path or nums[i] >= path[-1]:
                    visited.add(nums[i])
                    backtrack(i + 1, path + [nums[i]])
        
        backtrack(0, [])
        return ans