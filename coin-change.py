class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def solve(amount,dic):
            if amount == 0:
                return 0
            if amount in dic:
                return dic[amount]
            
            res = float('inf')

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res,solve(amount-coin,dic))

            dic[amount] = res + 1
            return res + 1
        res=solve(amount,{})
        if res == float('inf'):
            return -1
        return res