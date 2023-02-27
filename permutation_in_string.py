class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter()
        s2_len = len(s1)
        
        for idx,val in enumerate(s2):
            c2[val] += 1
            
            if idx >= s2_len:
                c2[s2[idx-s2_len]] -= 1
            
            if c1 == c2: 
                return True
        
        return False


