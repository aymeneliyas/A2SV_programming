class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        arr = []
        if n < 2:
            return 2
        for i in range(1,n+1):
            arr.append(2*i)

        length = len(arr)
        for i in range(length+1):
            if n in arr:
                return n
            n *= 2 
        return 0
