class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ans = 0
        pl = 0
        tr = 0
        players.sort()
        trainers.sort()
        while tr < len(trainers) and pl < len(players):
            if players[pl] <= trainers[tr]:
                ans += 1
                pl += 1
                tr += 1
            else:
                tr += 1
        return ans
