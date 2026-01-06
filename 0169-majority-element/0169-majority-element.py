class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f=int(len(nums)/2)
        dict1= {}
        for i in nums:
            if i in dict1:
                dict1[i] +=1
            else:
                dict1[i] =1
        
        for i,j in dict1.items():
            if j > f:
                return i

        
