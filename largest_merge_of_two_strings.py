class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans = ""
        left = 0
        right = 0
        while left < len(word1) and right < len(word2):
            if word1[left:] >= word2[right:]:
                ans = ans + word1[left]
                left += 1
            else:
                ans = ans + word2[right]
                right += 1
        while left < len(word1):
            ans = ans + word1[left]
            left += 1
        while right < len(word2):
            ans = ans + word2[right]
            right += 1
        return ans
