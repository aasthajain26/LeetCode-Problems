class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i,e in enumerate(nums):
            if target - e  in dict1:
                return [i, dict1[target - e]]
            else:
                dict1[e]=i
