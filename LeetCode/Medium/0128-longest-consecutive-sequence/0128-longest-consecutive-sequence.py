class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        a= set(nums)
        cnt =0
        sum1 = 0

        for i in a:
            if i-1 in a:
                pass
            else:
                cnt+=1
                while(i+1 in a ):
                    cnt +=1
                    i +=1
                sum1 = max(sum1,cnt)
                cnt =0
        return sum1

            


