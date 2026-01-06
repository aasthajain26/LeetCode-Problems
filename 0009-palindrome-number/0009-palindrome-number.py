class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        y=0
        z=x
        while(x>0):
            rem = x % 10 
            y = y*10 +  rem
            x = x//10
        
        if z!=y:
            return False
        
        return True

