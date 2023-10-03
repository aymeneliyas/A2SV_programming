class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        arr = []
        for key,[citya,cityb] in enumerate(costs):
            arr.append((citya-cityb,key))
        
        arr.sort()
        for key,[_,index] in enumerate(arr):
            if key < len(costs) // 2:
                total += costs[index][0]
            else:
                total += costs[index][1]
        return total