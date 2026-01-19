class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sum1 = 0
        sum12= float('-inf')
        for i in range(len(nums)):
            if sum1<0:
                sum1 =0

            sum1=sum1+nums[i]
            sum12 = max(sum1,sum12)

        return sum12