class TrieNode:
    def __init__(self,val):
        self.kids = {}
        self.eow = False
class Solution:
    def __init__(self):
        self.root = TrieNode('*')
    
    def insert(self,word):
        node = self.root
        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode(ch)

            node = node.kids[ch] 
        node.eow = True

    def search(self,word):
        node = self.root

        s = ""
        for ch in word:
            if ch in node.kids and node.kids[ch].eow == True:
                s += ch
            else:
                break
            node = node.kids[ch]
        return s
 
    def longestWord(self, words: List[str]) -> str:
        trie = Solution()
        for ch in words:
            trie.insert(ch)
        arr = []
        maxi = 0
        for ch in words:
            val = trie.search(ch)
            arr.append(val)
            maxi = max(maxi,len(val))
        
        ans = []
        for i in arr:
            if len(i) == maxi:
                ans.append(i)
        
        
    
        ans.sort(reverse = True)
        return ans[-1]