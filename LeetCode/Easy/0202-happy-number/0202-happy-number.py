class Solution:
    def isHappy(self, n: int) -> bool:
        if n <=0:
            return False
        l = set()

        while(n!=1):
            if n in l:
                return False
            l.add(n)
            s=0
            while(n!=0):

                a= n%10
                s += a*a 
                n = n//10
            n = s

            

        return True
        