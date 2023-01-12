from collections import defaultdict
from collections import Counter
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dir_map = defaultdict(list)
        ans = []
        for dir in paths:
            files = dir.split()
            
            for f in range(1,len(files)):
                val = files[f].split('(')
                dirs = files[0]+ '/' +val[0]
                
                    # key = list(filter(lambda x: dir_map[x] == val[1][:-1], dir_map))[0]
                    # ans.append(dirs)
                dir_map[val[1][:-1]].append(dirs)
                
        ans = []
        for val in dir_map.values():
            if len(val) > 1:
                ans.append(val)
        return ans
