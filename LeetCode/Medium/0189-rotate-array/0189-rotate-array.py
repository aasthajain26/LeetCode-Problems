class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_a(nums,s,e):

            while(s<=e):
                nums[s],nums[e] = nums[e],nums[s]
                s +=1
                e -=1
            return nums
        
        l = len(nums)
        k =k %l
        j = l -k -1
        reverse_a(nums,0,j)
        reverse_a(nums,j+1,l-1)
        reverse_a(nums,0,l-1)

        return nums