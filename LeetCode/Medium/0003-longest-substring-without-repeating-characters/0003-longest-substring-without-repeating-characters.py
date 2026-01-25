class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        i = 0 
        j = i+1
        ln = 1
        cnt =1
        st= set()
        while(j < len(s)):
           
            st.add(s[i])
            if s[j] in st:
                ln = max(ln, cnt )
                cnt= 1
                i+=1
                j =i+1
                st= set()
            else:
                st.add(s[j])
                j  +=1
                cnt +=1
                ln = max(ln, cnt )

        return ln 