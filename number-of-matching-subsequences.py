class TrieNode:
    def __init__(self):
        self.kids = {}
        
class Trie:
    def __init__(self,s):
        self.root = TrieNode()
        self.dic = defaultdict(list)
        for i in range(len(s)):
            self.dic[s[i]].append(i)

    def insert(self,word):
        node = self.root
        for chr in word:
            if chr not in node.kids:
                node.kids[chr] = TrieNode()
            node = node.kids[chr]

    def prefix(self,word):
        node = self.root
        idx = -1
        for chr in word:
            tmp = bisect_left(self.dic[chr], idx)
            if tmp == len(self.dic[chr]) or (idx > self.dic[chr][tmp]):
                return False
            idx = self.dic[chr][tmp] + 1
            node = node.kids[chr]
        return True
class Solution:

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie(s)
        for word in words:
            trie.insert(word)

        count = 0
        for word in words:
            if trie.prefix(word):
                count += 1
        
        return count