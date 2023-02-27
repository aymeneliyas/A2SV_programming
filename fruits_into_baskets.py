class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = 0
        left = 0
        
        seen = defaultdict(int)
        for right in range(len(fruits)):
            seen[fruits[right]] += 1
            while len(seen) > 2:
                seen[fruits[left]] -= 1

                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left += 1
            window = max(window,right-left+1)
        return window
