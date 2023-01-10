from collections import defaultdict
class Solution(object):
def printVertically(self, s):
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
