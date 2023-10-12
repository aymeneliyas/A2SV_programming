class Solution:
    def numTeams(self, rating: List[int]) -> int:
        left = [0] * len(rating)
        right = [0] * len(rating)
        ans = 0
        for i in range(len(rating)):
            count = 0
            count2 = 0
            for j in range(i):
                if rating[i] > rating[j]:
                    count += 1
                    ans += left[j]
                else:
                    count2 += 1
                    ans += right[j]
            left[i] = count
            right[i] = count2
        
        return ans