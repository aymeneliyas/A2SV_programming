class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        w = []
        for word in words:
            arr = list(word)
            arr.sort()
            count = Counter(word)
            w.append(count[arr[0]])
        
        w.sort()
        answer = []
        for key,query in enumerate(queries):
            arr = list(query)
            arr.sort()
            count = Counter(query)
            value = count[arr[0]]

            left = -1
            right = len(w)

            while left+1 < right:
                middle = left + (right-left) // 2
                if w[middle] > value:
                    right = middle
                elif w[middle] <= value:
                    left = middle

            answer.append(len(w)-right)
        return answer