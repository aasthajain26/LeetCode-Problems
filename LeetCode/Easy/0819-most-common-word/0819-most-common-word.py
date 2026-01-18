class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        r =""
        dict1={}
        for i in paragraph:
            if i.isalnum():
                r += i.lower()

            else:
                if r not in dict1 and r != "" and r not in banned:
                    dict1[r] = 1
                else:
                    if r not in banned and r != "":
                        dict1[r] +=1
                r =""
        if r not in dict1 and r != "" and r not in banned:
                    dict1[r] = 1
        else:
            if r not in banned and r != "":
                dict1[r] +=1

        m=float('-inf')
        el = ""
        for i,e in dict1.items():

            if e > m:
                m=e
                el = i
        return el 
