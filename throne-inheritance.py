class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.dic = defaultdict(list)
        self.dead = set()
    def birth(self, parentName: str, childName: str) -> None:
        self.dic[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        arr = set()
        def dfs(node,ans):
            arr.add(node)
            if node not in self.dead:
                ans.append(node)
            for ver in self.dic[node]:
                if ver not in arr:
                    dfs(ver,ans)
        dfs(self.king,ans)   
        return ans
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()