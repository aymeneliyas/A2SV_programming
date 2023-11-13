class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res ,dic = set(),set()
        for i in range(len(s)-9):
            word = s[i:i+10]
            if word in dic:
                res.add(word)
            dic.add(word)
        return res