class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict()
        for i in range(len(s)):
            dic[s[i]] = i+1
        ans = []
        left = 0
        right = 0 
        while left < len(s):
            partition = dic[s[left]] - left
            print(left)
            right = left+1
            check = dic[s[left]]
            while right < left + partition:
                if dic[s[right]] > check:
                    partition = dic[s[right]] - left
                    check = dic[s[right]]
                right += 1

            
            left += partition
            ans.append(partition)
        return ans
