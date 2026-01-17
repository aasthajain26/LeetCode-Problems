class Solution:
    def isValid(self, s: str) -> bool:
        dict1={
            ')':'(',
            '}':'{',
            ']':'['

        }
        stk=[]

        for i in s:
            if i in ('(','{', '['):
                stk.append(i)
            else:
                if len(stk)==0:
                    return False
                else:
                    a=stk.pop()
                    if a !=dict1[i]:
                        return False

        if len(stk) != 0:
            return False
        return True
