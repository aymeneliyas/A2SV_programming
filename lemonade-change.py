class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)

        for bill in bills:
            if bill == 5:
                change[5] += 1
            if bill == 10:
                if change[5] == 0:
                    return False
                change[10] += 1
                change[5] -= 1
            if bill == 20:
                if change[10] >= 1 and change[5] >= 1:
                    change[10] -= 1
                    change[5] -= 1
                    continue
                elif change[5] >= 3:
                    change[5] -= 3
                    continue
                else:
                    return False

        return True