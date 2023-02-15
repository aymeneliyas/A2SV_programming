# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        prev = head
        while curr.next != None:
            count += 1
            curr = curr.next
        count +=1
        itr = count - n - 1
        if count == 1 and n == 1:
            del(head)
            return 
        if count == n:
            head = head.next
            return head
        for _ in range(itr):
            prev = prev.next
        if prev.next and prev.next.next:
            prev.next = prev.next.next
        else:
            prev.next = None

        return head
