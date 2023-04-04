class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        for i in range(len(words)):
            mask = 0
            for j in words[i]:
                mask |= 1 << ord(j) - ord('a')
            masks.append(mask)
        
        ans = 0
        n = len(words)
        for i in range(n):
            for j in range(i):
                if (masks[i] & masks[j]) == 0:
                    val = len(words[i]) * len(words[j])
                    ans = max(ans,val)
        return ans