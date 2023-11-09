class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        store = defaultdict(int)
        val = 0
        winners = []
        for win,lose in matches:
            store[lose] += 1
            winners.append(win)
        res1,res2 = [],[]
        for key,val in store.items():
            if val == 1:
                res2.append(key)
        
        for i in winners:
            if store[i] == 0:
                res1.append(i)
                
        res1 = list(set(res1))
        res1.sort()
        res2.sort()
        return [res1,res2]
        
        