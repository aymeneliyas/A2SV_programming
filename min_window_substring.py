class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): 
            return ""
        
        ans = ""
        maps = defaultdict(int)
        counter = Counter(t)
        count = len(s) + 1
        matched = 0
        
        left = 0
        
        for right in range(len(s)):
            if s[right] in counter:
                maps[s[right]] += 1
                if maps[s[right]] == counter[s[right]]:
                    matched += 1
                
                
            while left <= right and matched == len(counter):
                    
                if count > (right - left + 1):
                    
                    ans = s[left:right+1]
                    count = len(ans)                    
                
                if s[left] in counter:
                    
                    maps[s[left]] -= 1
                    
                    if maps[s[left]] < counter[s[left]]:
                        matched -= 1
                    
                    if maps[s[left]] == 0:
                        del maps[s[left]]
                        
                left += 1
