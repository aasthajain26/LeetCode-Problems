class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = mx = nums[0]
        for i in nums[1:]:
            if i < 0 :
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(i, max_prod * i)
            min_prod = min(i, min_prod * i)

            mx = max(mx, max_prod)
            

        return mx
