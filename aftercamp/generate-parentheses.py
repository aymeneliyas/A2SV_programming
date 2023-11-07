class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def rec(opn,close,val):
            if opn == n and close == n:
                ans.append("".join(val))
                return 
            if opn == n:
                rec(opn,close+1,val + [")"])
            else:
                if opn > close:
                    rec(opn+1,close,val + ["("])
                    rec(opn,close+1,val + [")"])
                else:
                    rec(opn+1,close,val + ["("])
        rec(0,0,[])    
        return ans