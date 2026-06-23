# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        cnt=0
        if head.next==None:
            return head
        while temp:
            cnt+=1
            temp=temp.next
        cnt=cnt//2
        cnt+=1
        temp=head
        nodecnt=0
        while temp:
            nodecnt+=1
            if nodecnt>=cnt:
                return temp
            temp=temp.next
