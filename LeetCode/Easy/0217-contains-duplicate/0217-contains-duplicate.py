class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dict1={}
        for i in nums:
            if i in dict1:
                dict1[i] +=1
            else:
                dict1[i] =1
        
        for i in dict1:
            if dict1[i] >1:
                return True

        return False

