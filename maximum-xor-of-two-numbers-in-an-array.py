class Solution:
    def __init__(self):
        self.root = {}
        self.maxi = 0

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}

            node = node[ch] 

    def maxxor(self,word,val):
        ans = ""
        node = self.root
        for i in word:
            if i == "1" and "0" in node:
                ans += "0"
                node = node["0"]
            elif i == "0" and "1" in node:
                ans += "1"
                node =node["1"]
            else:
                ans += i
                node = node[i]
        
        self.maxi = max(self.maxi, int(ans,2)^val)

    def findMaximumXOR(self, nums: List[int]) -> int:
        trie=Solution()

        for i in nums:
            word="{:032b}".format(i)
            trie.insert(word)

        for i in nums:
            word="{:032b}".format(i)
            trie.maxxor(word,i)
        return trie.maxi