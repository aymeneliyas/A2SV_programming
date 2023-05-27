class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        arr = [0,1] + [0] * (n-1)
        for i in range(1,n+1):
            if 2 * i <= n:
                arr[2 * i] = arr[i]
            if 2 * i + 1 <= n:
                arr[2 * i + 1] = arr[i] + arr[i + 1]
        
        return max(arr)