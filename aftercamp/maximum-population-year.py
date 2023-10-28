class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0] * 2051
        for birth,death in logs:
            arr[birth] += 1
            arr[death] -= 1
        
        prefix = []
        current_sum = 0

        for num in arr:
            current_sum += num
            prefix.append(current_sum)
        
        m = max(prefix)
        ans = 0
        for key,val in enumerate(prefix):
            if val == m:
                ans = key
                break
        


        return ans