class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        half = 2 ** (n-1) / 2
        if k > half:
            if self.kthGrammar(n-1,(k-1) % half+1) == 0:
                return 1
            if self.kthGrammar(n-1,(k-1) % half+1) == 1:
                return 0
        else:
            return self.kthGrammar(n-1, k)