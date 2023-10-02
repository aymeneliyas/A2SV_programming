class TrieNode:
    def __init__(self,val):
        self.kids = {}
        self.val = val
        self.eow = False
        self.count = 0


class Solution:
    def __init__(self):
        self.root = TrieNode('*')
    
    def insert(self,word):
        node = self.root
        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode(ch)
            node.count += 1
            node = node.kids[ch]
        node.eow = True
        node.count += 1

    
    def prefix(self,word):
        ans = 0
        node = self.root
        for ch in word:
            node = node.kids.get(ch)
            if not node:
                return ans
            ans += node.count
        return ans

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Solution()
        for i in words:
            trie.insert(i)
        
        ans = []
        for i in words:
            val = trie.prefix(i)
            ans.append(val)
        return ans