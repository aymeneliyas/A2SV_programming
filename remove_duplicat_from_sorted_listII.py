# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        node = t = ListNode()
        l = []
        while curr is not None:
            l.append(curr.val)
            curr = curr.next
        
        d = Counter(l)
        for key, value in d.items():
            if value == 1:
                node.next = ListNode(key)
                node = node.next
                
        return t.next
