class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        start = dummy
        
        startNode = dummy
        for _ in range(left-1):
            startNode = startNode.next
        prev = startNode.next
        curr = prev.next
        nextNode = startNode.next
        
        for _ in range(left,right):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        startNode.next = prev
        nextNode.next = curr

        
        return dummy.next
