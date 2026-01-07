class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
       
        s= ""
        dict1 ={}
        for i in paragraph :
            if i.isalnum():
                s = s+ i.lower()
            else:
                if s not in dict1:
                    dict1[s] = 1
                else:
                    dict1[s] += 1
                s =""
        if s not in dict1:
            dict1[s] = 1
        else:
            dict1[s] += 1
        s =""
        
        for i in banned:
            if i in dict1:
                del dict1[i]
        
        el=None
        m=0
        for i,e  in dict1.items():
            if e > m:
                el= i 
                m=e

        return el