class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_length = len(t)
        for i in range(t_length-1):
            if t[i] in s:
                s = s.replace(t[i],'',1);
            elif t[i] not in s:
                return t[i]
        
        return t[-1]
