class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = defaultdict(list)
        dic2 = defaultdict(list)
        
        for i in range(len(s)):
            dic2[t[i]].append(s[i])
            dic[s[i]].append(t[i])

        
        for key,val in dic.items():
            
            if len(val) > 1 and len(set(val)) != 1:
                return False
        for key,val in dic2.items():
            
            if len(val) > 1 and len(set(val)) != 1:
                return False
        return True
        