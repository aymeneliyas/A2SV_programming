class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = [(ages[i],scores[i]) for i in range(len(scores))]

        arr.sort()
        dp = [0] * len(scores)
        for i in range(len(arr)):
            dp[i] =  arr[i][1]
            for j in range(i):
                if arr[i][1] >= arr[j][1]:
                    tmp = dp[j] + arr[i][1]
                    if tmp > dp[i]:
                        dp[i] = tmp
        
        print(dp)
        return max(dp)