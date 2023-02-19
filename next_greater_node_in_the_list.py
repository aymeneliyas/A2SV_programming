# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack = []
        
        curr = 0
        while head is not None:
            ans.append(0)
            current_value = head.val
            while stack and stack[-1][0] < current_value:
                val = stack.pop()
                ans[val[1]] = current_value
            stack.append((current_value, curr))
            curr += 1
            head = head.next
        return ans
