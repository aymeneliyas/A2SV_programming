class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)-1
        right = sum(weights)+1

        while left+1 < right:
            middle = math.floor(left + (right-left)/2)
            currentDay = self.getDays(middle,weights,len(weights))
            # print(middle,left,right,currentDay)
            if currentDay <= days:
                right = middle
            else:
                left = middle
        return left+1
            


    def getDays(self,weight,weights,n):
        days = 0
        current =0
        for i in range(n+1):
            if i < n and current+weights[i] <= weight:
                current += weights[i]
            else:
                days += 1
                if i == n:
                    break
                else:
                    current = weights[i]
        return days