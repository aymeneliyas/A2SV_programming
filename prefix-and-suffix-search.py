class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.dic = {}
        for key,word in enumerate(self.words):
            pre = ""
            for i in range(len(word)):
                pre += word[i]
                for j in range(0,len(word)):
                    suf = word[j:]
                    if suf != '':
                        self.dic[(pre,suf)] = key
    
    def f(self, pref: str, suff: str) -> int:
        
        if (pref,suff) in self.dic:
            return self.dic[(pref,suff)]
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)