class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        ans = 0
        len1 = len(words)
        for i in range(0,len1):
            word1 = set(words[i])
            for j in range(i+1,len1):
                word2 = set(words[j])
                if word1 == word2:
                    ans += 1
                
        return ans
