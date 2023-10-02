class TrieNode:
    def __init__(self):
        self.kids = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode()
            node = node.kids[ch]
        node.isEnd = True
    
    
    def search(self, word: str) -> bool:
        node = self.root
        def rec(start,cur):
            if start == len(word):
                if cur.isEnd:
                    return True
                else:
                    return False
            
            if word[start] == ".":
                for key,val in cur.kids.items():
                    if rec(start+1,val):
                        return True
                return False
            elif word[start] in cur.kids:
                if rec(start+1,cur.kids[word[start]]):
                    return True
            else:
                return False
        
        return rec(0,node)
        
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)