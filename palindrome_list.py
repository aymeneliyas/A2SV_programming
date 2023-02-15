# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        fast = head
        slow = head
        curr = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            temp = curr.next
            curr.next = prev
            prev = curr
            curr= temp
        
        if not fast:
            while curr and prev:
                if curr.val != prev.val:
                    
                    return False
                curr = curr.next
                prev = prev.next
        else: 
            curr = curr.next
            while curr and prev:
                if curr.val != prev.val:
                    return False
                curr = curr.next
                prev = prev.next

        return True
