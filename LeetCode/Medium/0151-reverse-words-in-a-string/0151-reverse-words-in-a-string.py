class Solution:
    def reverseWords(self, s: str) -> str:
        
        def reverse_s(s,i,j):
            a=s
            while(i<=j):
                a[i],a[j]=a[j],a[i]
                i +=1
                j -=1
            
            return a
        
        
        s= s.split()
    
        
        return " ".join(reverse_s(s,0,len(s)-1))