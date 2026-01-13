class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        maxcnt =0

        for i in nums:
            if i !=1:
                cnt =0
            else: 
                cnt +=1
            maxcnt = max(maxcnt, cnt)

        return maxcnt