# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        p = head
        q = head.next
        temp = None
        while(q is not None):
            temp = q.next
            q.next = p
            if p == head:
                p.next = None
            p = q
            q = temp
        return p

        