class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        k=x
        if x<0:
            return False
        else:
            while x>0:
                r=x%10
                rev=rev*10+r
                x//=10
            if k==rev:
                return True
            else:
                return False