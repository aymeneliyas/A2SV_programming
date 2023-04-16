class Solution:
    def findCenter(self, e: List[List[int]]) -> int:
        edge = set()

        for src,des in e:
            if src in edge: 
                return src
            if des in edge: 
                return des
            
            edge.add(src)
            edge.add(des)