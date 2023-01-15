from collections import defaultdict
from collections import Counter
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        words_map = defaultdict(int)
        len_words = len(words)
        length = len(words[0])
        for char in words[0]:
            words_map[char] += 1
        """
        b:1
        e:1
        l:2
        a:1
        """
        for key,count in words_map.items():
            for word in words:
                count = Counter(word)
                # print(word,count)
                if key not in word and words_map[key]:
                    words_map.pop(key)
                else:
                    if count[key] < words_map[key]:
                        words_map[key] = count[key]
        ans = []           
        for key in words_map.keys():
            for i in range(words_map[key]):
                ans.append(key)
        return ans
