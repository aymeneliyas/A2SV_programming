class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.arr = [-1] * k
        self.head = -1
        self.tail = -1      

    
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = 0
            self.tail = 0
            
            self.arr[self.tail] = value
        else:
            self.tail = (self.tail + 1) % self.k
            self.arr[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.tail == self.head:
            self.arr[self.head] = -1
            self.head = -1
            self.tail = -1
        else:
            self.arr[self.head] = -1
            self.head = (self.head + 1) % self.k
        
        return True
            

    def Front(self) -> int:
        return self.arr[self.head]

    def Rear(self) -> int:
        return self.arr[self.tail]
        

    def isEmpty(self) -> bool:
        return self.head == -1 and self.tail == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % self.k == self.head      


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()