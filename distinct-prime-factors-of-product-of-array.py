class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            d = 2

            while d * d <= num:
                while num % d == 0:
                    res.append(d)
                    num //= d
                d += 1
            if num > 1:
                res.append(num)
        
        return len(set(res))