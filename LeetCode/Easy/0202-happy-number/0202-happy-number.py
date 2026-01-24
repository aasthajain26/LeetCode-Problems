class Solution:
    def isHappy(self, n: int) -> bool:
        if n <=0:
            return False
        l = set()
        s =0
        while(n!=1):

            l.add(n)
            while(n!=0):

                a= n%10
                s += a*a 
                n = n//10

            if s in l:
                return False

            n =s
            s=0
            

        return True
        