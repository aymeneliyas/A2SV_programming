class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        result = False
        @cache
        def rec(i,j):
            if i + j >= len(s3):
                return True

            result = False
            if i<len(s1) and s3[i+j] == s1[i]:
                result = result or rec(i+1,j) 
            if j<len(s2) and s3[i+j] == s2[j]:
                result = result or rec(i,j+1)
            
            return result
        if len(s1) + len(s2) > len(s3):
            return False
        return rec(0,0)