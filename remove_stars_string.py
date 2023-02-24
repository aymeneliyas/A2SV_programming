class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for word in s:
            if word == "*":
                stack.pop()
            else:
                stack.append(word)
        return "".join(stack)
