class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        odd = 0
        wordsSet = set(words)
        ans = 0
        count = Counter(words)

        for key,value in count.items():
            val = key[1] + key[0]
            if key[0] != key[1]:
                ans += min(count[key],count[val]) * 2
            
            if key[0] == key[1]:
                if value % 2 == 1:
                    odd += 1
                    ans += (value -1) * 2
                else:
                    ans += (value) * 2
        if odd:
            ans += 2  
        return ans
     
            

        if odd:
            ans += 2
        return ans
