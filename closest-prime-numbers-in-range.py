class Solution:
    def getprimes(self,left,num):
        primes = [True for i in range(num+1)]
        primes[0] = primes[1] = False
        d = 2
        while d*d <= num:
            j = d*d
            if primes[j]:
                while j <= num:
                    primes[j] = False
                    j += d
            d += 1
        primeNums = []

        for index,isPrime in enumerate(primes):
            if isPrime and index >= left:
                primeNums.append(index)
        return primeNums

    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = self.getprimes(left,right)
        low = 0
        if len(arr) < 2:
            return [-1,-1]

        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) < (arr[low+1] - arr[low]):
                low = i
        return [arr[low],arr[low+1]]