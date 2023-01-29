class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """
        1 2 3 3 4 5 
        """
        skill.sort()
        left = 0
        right = len(skill)-1
        out = skill[right] + skill[left]
        ans = 0
        while left < right:
            if skill[right] + skill[left] != out:
                return -1
            else:
                ans += skill[right] * skill[left]
            left += 1
            right -= 1
        return ans
