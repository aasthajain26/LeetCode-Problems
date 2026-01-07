class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ==0:
            return False
        rem=0
        while (n>1 and rem==0):
            rem= n%2 
            n= n//2 
            print(rem,n)
            
        
        if n ==1 and rem ==0:
            return True
        if rem !=0:
            return False
        return True
        
