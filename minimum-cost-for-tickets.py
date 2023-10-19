class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def rec(index):
            if index >= len(days):
                return 0
            
            idx1 = index + 1
            idx2 = bisect_right(days,days[index]+6)
            idx3 = bisect_right(days,days[index]+29)

            val1 = costs[0] + rec(idx1)
            val2 = costs[1] + rec(idx2)
            val3 = costs[2] + rec(idx3)

            return min(val1,val2,val3)

        return rec(0)