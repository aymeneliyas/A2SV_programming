class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            w = sorted(word)
            w = "".join(w)
            dic[w].append(word)
        
        ans = []
        for key,val in dic.items():
            ans.append(val)
        return ans