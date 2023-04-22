class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        unique = ['']
        ans = 0
        for i in range(len(arr)):
            size = len(uniqELements)
            for j in range(size):
                x=arr[i]+uniqELements[j]
                if (len(x)==len(set(x))):
                    uniqELements.append(x)
                    ans = max(ans,len(x))

        return ans