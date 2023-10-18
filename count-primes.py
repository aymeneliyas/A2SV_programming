class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        prime = [True for _ in range(n+1)]
        p = 2
        while p * p <= n:
            # If prime[p] is not changed, then it is a prime
            if prime[p]:
                # Update all multiples of p
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        
        prime = prime[2:]
        prime.pop()
        count = 0
        for b in prime:
            if b:
                count += 1
        return count