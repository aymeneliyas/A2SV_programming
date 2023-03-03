class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        e/../home
        /home
        """
        d = path.split("/")
        stack = []
        for i in d:
            if len(i) > 0 and i != ".":
                if i != "..":
                    stack.append(i)
                if stack and i == "..":
                    stack.pop()
        return "/" + "/".join(stack)