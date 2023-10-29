class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1

        @cache    
        def rec(a,b):
            if a <= 0 and b > 0:
                return 1
            if a <= 0 and b <= 0:
                return 0.5
            
            if b <= 0 and a > 0:
                return 0
            
            
            ans1 = rec(a-100,b)
            ans2 = rec(a-75,b-25)
            ans3 = rec(a-50,b-50)
            ans4 = rec(a-25,b-75)

            return 0.25 * (ans1 + ans2 + ans3 + ans4)
        
        return rec(n,n)


