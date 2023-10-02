class TrieNode:
    def __init__(self,val):
        self.kids = {}
        self.val = val
        self.eow = False
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode('*')

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for ch in key:
            if ch not in node.kids:
                node.kids[ch] = TrieNode(ch)
            node = node.kids[ch]
        node.eow = True
        node.value = val   

    
    def sum(self, prefix: str) -> int:
        node = self.root
        def dfs(root):
            summ = root.value

            for ch in root.kids:
                val = dfs(root.kids[ch])
                summ += val
            
            return summ

        for ch in prefix:
            if ch not in node.kids:
                return 0
            node = node.kids[ch]
        return dfs(node)




# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)