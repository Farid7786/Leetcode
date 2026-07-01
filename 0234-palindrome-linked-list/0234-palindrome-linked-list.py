# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        front = head
        last = head
        stop=False
        def pali(last):
            nonlocal front
            nonlocal stop
            if not last:
                return
            pali(last.next)
            if front.val!=last.val:
                stop=True
            front=front.next
        pali(last)
        print(stop)
        if stop:
            return False
        else:
            return True
        