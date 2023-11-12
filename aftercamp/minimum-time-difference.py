class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time_point in timePoints:
            hours, mins = map(int, time_point.split(':'))
            minutes.append(hours * 60 + mins)

        print(minutes)
        minutes.sort()

        ans = float('inf')
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            ans = min(ans, diff)

      
        last_diff = (24 * 60 - minutes[-1]) + minutes[0]
        ans = min(ans, last_diff)

        return ans



