class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        counter = 0
        while num:
            temp = 0
            val = num & 1
            if val == 0:
                temp = 1
            
            ans += temp << counter
            counter += 1
            num = num >> 1 
        return ans