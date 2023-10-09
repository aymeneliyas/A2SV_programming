class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = []
        for i in range(len(gas)):
            ans.append(gas[i]-cost[i])
        
        if sum(ans) < 0:
            return -1
        tank = 0
        start = 0
        for idx,pr in enumerate(ans):
            tank += pr
            if tank < 0:
                tank = 0
                start = idx+1
        return start