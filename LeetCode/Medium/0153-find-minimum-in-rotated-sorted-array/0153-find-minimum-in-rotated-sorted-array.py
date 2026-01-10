class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0 
        high = len(nums) -1
        a= nums[(low+high) //2]
        while(low<=high):

            mid =( low+high) //2
            
            if nums[low] <= nums[mid]:
                if a >nums[low]:
                     a = nums[low]
                low = mid+1
            else:
                
                if nums[mid] <= nums[high]:
                    if a >nums[mid]:
                        a = nums[mid]
                    high = mid-1
                else:
                    high = mid -1
            
        return a

