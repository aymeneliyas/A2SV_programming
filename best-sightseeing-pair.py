class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        i = 0
        answer = 0
        size = len(values)
        for j in range(i+1,size):
            answer = max(answer,values[i]+values[j]+i-j)
            if values[j] + j-i > values[i]:
                i = j
        return answer