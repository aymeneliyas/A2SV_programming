# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = head
        prev = head
        curr = prev.next
        even = prev.next
        
        while curr and curr.next:
            prev.next = curr.next
            
            curr.next = curr.next.next
            prev.next.next = even
        
            prev = prev.next
            curr = curr.next
            # print(dummy)
        return dummy
