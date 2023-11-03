class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for val in asteroids:
            flag = True
            if val < 0:
                if not stack:
                    stack.append(val)
                else:
                    a = stack.pop()
                    if a > abs(val):
                        stack.append(a)
                        continue
                    if a == abs(val):
                        continue
                    while abs(val) > a:
                        if a < 0:
                            flag = False
                            stack.append(a)
                            stack.append(val)
                            break
                        if not stack:
                            flag = False
                            if abs(val) > a:
                                stack.append(val)
                            else:
                                stack.append(a)
                            break 
                        a = stack.pop()
                    if flag:
                        if a != abs(val):
                            stack.append(a)
            else:
                stack.append(abs(val))
        
        return stack