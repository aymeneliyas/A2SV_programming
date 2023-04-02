class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        val = bin(n)[2:]

        for i in range(len(val)-1):
            if val[i] == val[i+1]:
                return False
        
        return True