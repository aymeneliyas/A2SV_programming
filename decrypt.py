class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        
        hs = set()
        
        for i in range(10, 27):
            hs.add(str(i) + "#")
        
        i = 0
        
        while i < len(s):
            if s[i:i+3] in hs:
                res += chr(int(s[i:i+2]) + 96)
                i += 3
            else:
                res += chr(int(s[i]) + 96)
                i += 1
        
        return res
    
