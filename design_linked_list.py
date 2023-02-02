class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head

        for i in range(0, index):
            current = current.next

        return current.value

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:        
        if index > self.size:
            return

        current = self.head
        newnode = Node(val)

        if index <= 0:
            newnode.next = current
            self.head = newnode
        else:
            for i in range(index - 1):
                current = current.next
            newnode.next = current.next
            current.next = newnode

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for i in range(0, index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
