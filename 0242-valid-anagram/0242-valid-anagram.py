class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        if len(s) != len(t):
            return False
    
        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1
        for i in t:
            if i not in dict_s :
                return False
            if i in dict_s:
                dict_s[i] -=1

        for i in dict_s:
            if dict_s[i]!=0:
                return False
        return True 




