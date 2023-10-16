class Solution:
    def countVowels(self, word: str) -> int:
        N = len(word)
        vowels = {"a", "e", "i", "o", "u"}
        counts = 0

        for i, c in enumerate(word):
            if c in vowels:
                counts += (i+1)*(N-i)
        
        return counts