class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        if n == 1:
            return 0

        def rec(dec,clip,cur):
            if cur > n:
                return float('inf')
            if cur == n:
                return 0
            
            if dec == "copy":
                memo[(dec,clip,cur)] =  1 + rec("paste",clip,cur + clip)
            else:
                memo[(dec,clip,cur)] =  min(1 + rec("copy",cur,cur), 1+rec("paste",clip,cur+clip))
            
            return memo[(dec,clip,cur)]
            
        return 1 + rec("copy",1,1)