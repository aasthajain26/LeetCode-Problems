class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        j=0
        for i in range(len(nums)-1):
            #print(i,nums[i],nums[i+1],j)
            if nums[i] >= nums[i+1]:
                j=i+1
                #print('j',j)
            
        return j


            
        