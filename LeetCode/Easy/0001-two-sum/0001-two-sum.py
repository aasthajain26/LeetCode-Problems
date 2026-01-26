class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}

        for i in range(len(nums)):
            a=target-nums[i]
            if a in dict1:
                return [i, dict1[a]]

            else:
                dict1[nums[i]]=i


            