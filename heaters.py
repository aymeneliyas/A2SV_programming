class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        for i in range(len(houses)-1, -1,-1):
            idx = bisect_left(heaters,houses[i])

            if idx > 0 and idx < len(heaters):
                ans = max(ans,min(abs(houses[i]-heaters[idx]) ,abs(houses[i]-heaters[idx-1])) )
            elif idx == 0:
                ans = max(ans,abs(houses[i]-heaters[idx]))
            elif idx == len(heaters):
                ans = max(ans,abs(houses[i]-heaters[idx-1]))
        return ans