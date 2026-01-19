class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        s = 0 
        e = len(numbers) -1 

        while(s<=e):
            
            if numbers[e]+numbers[s]== target:
                return s+1, e+1

            elif numbers[e]+numbers[s] > target:
                 e-=1
            else:
                s +=1
            