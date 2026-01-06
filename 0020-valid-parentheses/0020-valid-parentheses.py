class Solution:
    def isValid(self, s: str) -> bool:
        a=[]

        if s[0] in (')','}',']') or len(s) == 1:
            return False

        for i in range(len(s)):
            
            if s[i] in ('(','{','['):
                a.append(s[i]) 
            
            if len(a)==0 and s[i] in (')',']','}'):
                return False
                
            if len(a)>0:
                if s[i]==')' and  a.pop() != '(' :
                    return False

                if s[i]=='}' and  a.pop() != '{' :
                    return False

                if s[i]==']' and  a.pop() != '[' :
                    return False

            

        if len(a)>0:
            return False
        return True
        
        