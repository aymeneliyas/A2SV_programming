class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+","*","-","/"]
        for tok in tokens:
            if tok not in op:
                stack.append(int(tok))
            else:
                right = stack.pop()
                left = stack.pop()
                if tok == "+":
                    tot = left + right
                if tok == "*":
                    tot = left * right
                if tok == "-":
                    tot = left - right
                if tok == "/":
                    tot = int(left / right)
                stack.append(tot)
        return stack[-1]