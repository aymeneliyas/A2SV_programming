class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}

        for key,val in enumerate(order):
            dic[val] = key
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if dic[word1[j]] > dic[word2[j]]:
                        return False
                    break;
        return True
