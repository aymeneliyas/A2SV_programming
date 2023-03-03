class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        ( 1 )
        """
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            if i == ")":
                temp = []
                val = stack.pop()
                while val != "(":
                    temp.append(val)
                    val = stack.pop()
                if len(temp) == 1:
                    if stack and stack[-1] != "(":
                        stack.append(stack.pop() + 2 * temp[0])
                    else:
                        stack.append(temp[0] * 2)
                elif len(temp) > 1:
                    if stack and stack[-1] != "(":
                        stack.append(stack.pop() + sum(temp))
                    else:
                        stack.append(sum(temp))
                else:
                    if stack and stack[-1] != "(": 
                        stack.append(stack.pop() + 1)
                    else:
                        stack.append(1)
                temp = []
        
        
        return stack[0]