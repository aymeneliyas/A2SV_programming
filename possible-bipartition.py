class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        color_dict = {}
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node,color):
            color_dict[node] = color
            
            for dislike in graph[node]:
                if dislike in color_dict:
                    if color_dict[dislike] == color:
                        return False
                else:
                    if not dfs(dislike,1-color):
                        return False
            return True
        
        for i in range(1,n+1):
            if i not in color_dict:
                if not dfs(i,1):
                    return False
        return True