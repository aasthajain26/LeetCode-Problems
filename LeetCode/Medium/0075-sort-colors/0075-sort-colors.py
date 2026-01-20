class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=0
        mid =0
        e = len(nums)-1
        
        while(mid<=e):

            if nums[mid] ==0:
                nums[s], nums[mid]= nums[mid], nums[s]
                s +=1
                mid +=1

            elif nums[mid]==1:
                mid +=1
            else:
                nums[mid], nums[e]= nums[e], nums[mid]
                e -=1 