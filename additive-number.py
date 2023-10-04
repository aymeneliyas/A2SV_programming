class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ans = []
        def rec(index,arr):
            if index >= len(num):
                ans.append(arr[:])

            for i in range(index,len(num)):
                w = num[index:i+1]
                if w[0] == "0" and len(w) > 1:
                    return 
                if len(arr) <= 1 or int(w) == int(arr[-1]) + int(arr[-2]):
                    arr.append(w)
                    rec(i+1,arr)
                    arr.pop()
            
            
        rec(0,[])
        print(ans)
        for arr in ans:
            if len(arr) > 2:
                return True
        return False