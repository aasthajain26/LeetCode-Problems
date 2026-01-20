class Solution:
    def trap(self, height: List[int]) -> int:
        lm =rm =0
        ans =0 
        l=0
        r = len(height) -1 

        while(l<r):
            lm = max(height[l], lm )
            rm = max(height[r], rm)

            if lm < rm:
                ans += lm- height[l]
                l+=1
            else:
                ans += rm - height[r]
                r -=1
        return ans
