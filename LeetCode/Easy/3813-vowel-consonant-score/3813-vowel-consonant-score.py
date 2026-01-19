class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        t=len(s)
        v =0
        score =0
        c =0
        for i in s:

            if i.isalpha() and i in ('a','e','i','o','u'):
                v +=1

            elif i.isalpha():
                c +=1
            else:
                continue


        if c >0:
            score =  v // c
        
        return score