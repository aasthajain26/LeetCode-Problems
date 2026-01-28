class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dict1={0: -1}

        sum1 = 0

        for i in range(len(nums)):
                #print(sum1,nums[i])
                sum1 +=nums[i] 
                #print(sum1 % k )
                rem=sum1 % k
                if  rem  in dict1:
                    if i - dict1[rem] >=2:
                         return True
                else:
                    dict1[rem] = i
                    
             
        return False
