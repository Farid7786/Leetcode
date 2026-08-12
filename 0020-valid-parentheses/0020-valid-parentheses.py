class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        top=-1
        for i in range(len(s)):
            if len(st)!=0:
                if (st[top]=="(" and s[i]==")") or (st[top]=="[" and s[i]=="]") or (st[top]=="{" and s[i]=="}"):
                    st.pop()
                    top-=1
                else:
                    st.append(s[i])
                    top+=1
            else:
                st.append(s[i])
                top+=1
        if len(st)==0:
            return True
        else:
            return False