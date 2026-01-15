class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
        max_sum=sum(nums[:k])
        new_sum= max_sum
        j=len(nums)

        for i in range(k, j):

            new_sum = new_sum + nums[i] - nums[i-k]
            max_sum = max(max_sum ,new_sum )

        return max_sum /k 