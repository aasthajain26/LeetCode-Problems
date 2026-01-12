class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max1=nums[0]
        for i in range(len(nums)):

            for j in range(i+1, len(nums)):
                max1 = max(max1, nums[i],nums[j])
                if max1<sum(nums[i:j+1]):
                    max1= max(sum(nums[i:j+1]), nums[i], nums[j])
                #print(nums[i], nums[j], nums[i:j],max1)
        return max1

