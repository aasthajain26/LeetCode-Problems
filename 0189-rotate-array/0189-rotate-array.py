class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate_array_right(arr,start,end):
            while (start<end):    
                arr[start],arr[end]= arr[end],arr[start]
                start +=1
                end -=1
                
        n= len(nums)
        k= k%n

        #reverse whole array
        rotate_array_right(nums,0,n-1)
        #reverse k elements from the start
        rotate_array_right(nums,0,k-1)
        #reverse all elements from the kth element
        rotate_array_right(nums,k,n-1)






