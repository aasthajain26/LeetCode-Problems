class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)-1
        k=0
        while(i<=j):
            if nums[i]!=0:

                nums[i],nums[k]=nums[k],nums[i]
                k +=1

            
            i +=1

        
