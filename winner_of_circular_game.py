class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        arr = []
        
        for i in range(1,n+1):
            arr.append(i)
        curr = len(arr) - 1
        while len(arr) > 1:
            curr = (curr + k ) % len(arr)
            arr.pop(curr)
            curr -= 1
        return arr[0]
               
        print(arr)
        return 0
