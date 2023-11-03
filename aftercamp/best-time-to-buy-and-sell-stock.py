class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        def rec(index,buy,tran):
            if index >= len(prices):
                return 0
            if (index,buy,tran) in dp:
                return dp[(index,buy,tran)]
                
            if tran <= 1:
                pas = rec(index+1,buy,tran)
                if buy:
                    val = rec(index+1,not buy,tran+1) - prices[index] 
                    dp[(index,buy,tran)] = max(pas,val)
                
                else:
                    val = rec(index+1,not buy,tran) + prices[index]
                    dp[(index,buy,tran)] = max(pas,val)
                return dp[(index,buy,tran)]
            else:
                return 0
        
        return rec(0,True,0)