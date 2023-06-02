class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def solve(index,flag):
            if index == len(prices):
                return 0
            
            if (index,flag) in memo:
                return memo[(index,flag)]
            
            skip = solve(index+1,flag)
            if not flag:
                hold = solve(index+1,True) - prices[index] - fee
            else:
                hold = solve(index+1,False) + prices[index]
            
            memo[(index,flag)] = max(skip,hold)
            maxi = max(skip,hold)
            return maxi

        return solve(0,False)