# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash={}
        c=0
        temp=head
        while temp:
            c+=1
            if temp in hash:
                return hash[temp]
            else:
                hash[temp]=temp
            temp=temp.next
        return None