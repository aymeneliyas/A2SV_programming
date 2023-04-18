class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        arr = set()
        ans = []

        for start,end in edges:
            arr.add(end)
        
        for ver in range(n):
            if ver not in arr:
                ans.append(ver)
                
        return ans