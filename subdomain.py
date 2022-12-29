from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain = defaultdict(int)
        for elm in cpdomains:
            splited = elm.split()
            length = len(splited[1])-1
            for i in reversed(range (length)):
                if splited[1][i] == '.':
                    domain[splited[1][i+1:]] += int(splited[0])
            domain[splited[1]] += int(splited[0])
            
        ans = list(map(lambda x : str(domain[x])+" "+str(x),domain))
        return ans
