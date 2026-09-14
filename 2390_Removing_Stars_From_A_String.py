class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        for ch in s:
            if ch!='*':
                st.append(ch)
            else:
                if st:
                    st.pop()
        return ''.join(st)
        
