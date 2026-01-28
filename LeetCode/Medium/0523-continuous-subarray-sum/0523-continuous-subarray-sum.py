class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dict1={0: -1}

        sum1 = 0

        for i in range(len(nums)):
                #print(sum1,nums[i])
                sum1 +=nums[i] 
                #print(sum1 % k )
                if sum1 % k not in dict1:
                    dict1[sum1 % k] = i
                else:
                    if i - dict1[sum1 % k] >=2:
                         return True
             
                

        return False
