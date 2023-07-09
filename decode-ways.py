class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s) : 1}        
        def dfs(idx):
            if idx in memo:
                return memo[idx]
            
            if s[idx] == "0":
                return 0
            
            res = dfs(idx+1)
            if (idx+1 < len(s) and (s[idx] == "1" or s[idx] == "2" and s[idx+1] in "0123456")):
                res += dfs(idx+2)
            memo[idx] = res
            return res
        return dfs(0)