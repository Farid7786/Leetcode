class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        c=False
        if -2**31<x<2**31-1:
            if x<0:
                x=abs(x)
                c=True
            while x>0:
                r=x%10
                rev=rev*10+r
                x//=10
            if c and (-2**31<rev<2**31-1):
                return -rev
            elif -2**31<rev<2**31-1:
                return rev
            else: 
                return 0
        else:
            return 0

