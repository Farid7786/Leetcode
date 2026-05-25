class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal=""
        if len(s)==1:
            return True
        for i in s:
            if i.isalpha() or i.isdigit():
                pal+=i
        pal=pal.lower()
        
        def pali(i):
            if i>=len(pal)//2:
                return True
            if pal[i]!=pal[len(pal)-i-1]:
                return False
            else:
                return pali(i+1)
        return pali(0)
        
            