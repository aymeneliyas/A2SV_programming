# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,left,right):
        dummy = node = ListNode()
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right 
                right = right.next
            node = node.next
        if left:
            node.next = left
        else:
            node.next = right
        return dummy.next

    def getMid(self,head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left,right)