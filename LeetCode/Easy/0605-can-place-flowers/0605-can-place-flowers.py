class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1 and flowerbed[0]==0:
            n=n-1
            return n<=0

        for i in range(len(flowerbed)):
            if flowerbed[i] ==1 :
                continue
            else:
                if i !=0 and i!=len(flowerbed)-1 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i] =1
                    n=n-1
                elif i==0 and flowerbed[i+1]==0:
                    flowerbed[i] =1
                    n=n-1
                elif i==len(flowerbed)-1 and flowerbed[i-1]==0:
                    flowerbed[i] =1
                    n=n-1
                else:
                    continue
            
 
        return n<=0
                
