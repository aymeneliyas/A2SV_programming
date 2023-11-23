class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        ans = []
        changed.sort()
        n = len(changed)
        if n%2:
            return []
        count = Counter(changed)
        
        for x in changed:
            if x==0 and count[x]>=2:
                count[x] -= 2;
                ans.append(x)
            elif x>0 and count[x] and count[x*2]:
                count[x] -= 1
                count[x*2] -= 1
                ans.append(x)
        return ans if len(ans) == n/2 else []