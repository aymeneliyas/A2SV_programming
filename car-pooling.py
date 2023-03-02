class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        big = 0
        for trip in trips:
            big = max(big,trip[2])
    
        prefix = [0] * (big + 2)

        for trip in trips:
            prefix[trip[1]] += trip[0]
            prefix[trip[2]] -= trip[0]

        ps = [prefix[0]]
        for p in range(len(prefix)):
            ps.append(ps[-1] + prefix[p])
    
        for p in ps:
            if p > capacity:
                return False
        return True