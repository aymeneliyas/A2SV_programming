class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for dr in logs:
            if dr == "../":
                if stack:
                    stack.pop()
            elif dr == "./":
                continue
            else:
                stack.append(dr)
                
        print(stack)
        return len(stack)
