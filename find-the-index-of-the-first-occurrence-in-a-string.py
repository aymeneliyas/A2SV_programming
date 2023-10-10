class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        dic = {}
        m = len(needle)
        n = len(haystack)
        for i in range(26):
            dic[chr(ord('a')+i)] = i
        # print(dic)
        if n < m:
            return -1
        nee = 0
        hay = 0
        mod = 10 ** 9 + 7
        for i in range(len(needle)-1,-1,-1):
            nee += (26 ** (m-i-1)) * dic[needle[i]]
            hay += (26 ** (m-i-1)) * dic[haystack[i]]
            nee %= mod
            hay %= mod
       
        if nee == hay:
            return 0
       
        for i in range(m,n):
            hay -= (26 ** (m-1)) * dic[haystack[i-m]]
            hay *= 26
            hay += dic[haystack[i]]
            hay %= mod
            
            if hay == nee:
                return (i-m)+1
        return -1