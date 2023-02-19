# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ptr = None
        forwrd = ListNode(0)
        twin1 = forwrd
        curr = head
        while curr:
            forwrd.next = ListNode(curr.val)
            temp = curr.next
            curr.next = ptr
            ptr = curr
            curr = temp
            forwrd = forwrd.next
        twin2 = ptr
        fast = twin1
        ans = 0
        twin1 = twin1.next
        while fast and fast.next:
            tot = twin1.val + twin2.val
            ans = max(tot,ans)
            fast = fast.next.next
            twin1 = twin1.next
            twin2 = twin2.next
        return ans

