class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        left = 0
        for right in range(len(s)):
            
            dic[s[right]] += 1
            most = max(dic.values())
            window = right - left + 1
            q = window - most
            if q > k:
                dic[s[left]] -= 1
                left += 1
        return len(s) - left