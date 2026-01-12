class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        st=[]
        res = [-1] * len(nums)
        for i in nums[::-1]:
            
            while st and i>st[-1]:
                st.pop()

            st.append(i)

        for i in range(len(nums)-1, -1,-1 ):
            
            
            while st and st[-1] <= nums[i]:
                st.pop()

            if st :
                    res[i] = st[-1]
            st.append(nums[i])

        return res