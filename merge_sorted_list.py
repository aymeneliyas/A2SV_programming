# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
[?12;2$y        head1 = list1
        head2 = list2
        ans = ans_head = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                g = ListNode(head1.val)
                ans.next = g
                head1 = head1.next
            else:
                g = ListNode(head2.val)
                ans.next = g
                head2 = head2.next
            ans = ans.next
        if head1:
            ans.next = head1
        elif head2:
            ans.next = head2
        return ans_head.next
