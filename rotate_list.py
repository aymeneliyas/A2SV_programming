# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        
        curr = head
        size = 1
        while curr.next:
            size+=1
            curr = curr.next
        
        k = k%size if k>=size else k
        
        if k==0:
            return head
        else:
            curr.next = head
        
        ctr = 1
        while ctr<size-k:
            head = head.next
            ctr+=1
        
        temp = head.next
        head.next = None
        return temp
