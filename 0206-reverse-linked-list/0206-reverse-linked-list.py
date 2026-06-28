# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        last=head
        front=head
        stop=False
        def recurse(last):
            nonlocal front
            nonlocal stop
            if not last:
                return
            recurse(last.next)
            if stop:
                return True
            if front==last or front.next==last:
                stop=True
            front.val,last.val=last.val,front.val
            front=front.next
        recurse(last)
        return head
