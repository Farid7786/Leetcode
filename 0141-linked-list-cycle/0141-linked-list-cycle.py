# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash={}
        temp=head
        while temp:
            if id(temp) in hash:
                return True
            hash[id(temp)]=1
            temp=temp.next
        return False