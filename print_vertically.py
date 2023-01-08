from collections import defaultdict
class Solution(object):
[2;2R[3;1R[>77;30500;0c]10;rgb:bfbf/bfbf/bfbf]11;rgb:0000/0000/0000    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        longest = 0
        result = []
        words = s.split()
        for word in words:
            longest = max(longest,len(word))
        for index in range(longest):
            arr = []
            for word in words:
                
                if index < len(word):
                    arr.append(word[index])
                else:
                    arr.append(' ')
            result.append(arr)
       
        answer = []
        for arr in result:
            answer.append("".join(arr).rstrip())
        return answer
