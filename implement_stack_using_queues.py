class MyStack:

    def __init__(self):
        self.arr = deque()
    
    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        temp = deque()
        while len(self.arr) > 1:
            temp.append(self.arr.popleft())
        ans = []
        if len(self.arr) > 0:
            ans.append(self.arr.pop())
        self.arr = temp
        return ans[0]

    def top(self) -> int:
        return self.arr[-1]

    def empty(self) -> bool:
        if len(self.arr) > 0:
            return False
        return True
