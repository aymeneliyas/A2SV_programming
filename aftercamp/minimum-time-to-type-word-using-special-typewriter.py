class Solution:
    def minTimeToType(self, word: str) -> int:
        cnt, prev = len(word), 'a'
        for cur in word:
            diff = abs(ord(cur) - ord(prev)) 
            cnt += min(diff, 26 - diff)
            prev = cur
        return cnt
        
