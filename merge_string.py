class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        l = 0
        rang = min(len(word1),len(word2))
        for i in range(rang):
            output += word1[i]
            output += word2[i]
            l += 1
            if l == len(word1):
                for j in range(i+1,len(word2)):
                    output += word2[j]
                break
            if l == len(word2):
                for j in range(i+1,len(word1)):
                    output += word1[j]
                break
        return output
