class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s)+1)
        for shift in shifts:
             
            if shift[2] == 0:
                arr[shift[0]] += -1
                arr[shift[1]+1] += 1
            elif shift[2] == 1:
                arr[shift[0]] += 1
                arr[shift[1]+1] += -1
        
        prefix = []
        for key,val in enumerate(arr):
            if key == 0:
                prefix.append(arr[key])
            else:
                prefix.append(prefix[key-1] + val)
        print(prefix)
        ans = ""
        for key,val in enumerate(s):
            n = ord(val) - ord("a") + prefix[key] + 26
            n = n % 26
            ans += chr(n+ord('a'))
        
        return ans