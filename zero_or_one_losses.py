from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers_map = defaultdict(int)
        winners_map = defaultdict(int)
        for match in matches:
            
            winners_map[match[0]] += 1
            losers_map[match[1]] += 1

        losers = []
        winners = []

        for elm in losers_map:
            if losers_map[elm] == 1:
                losers.append(elm)
            

        for elm in winners_map:
            if losers_map[elm] == 0:
                winners.append(elm)
        winners.sort()
        losers.sort()
        
        print(winners_map)
        return [winners,losers]
