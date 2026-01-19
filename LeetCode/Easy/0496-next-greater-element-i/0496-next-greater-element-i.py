class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={}
        for i,e in enumerate(nums1):
            dict1[e]=i

        res = [-1] * len(nums1)
        stk = []
        for i in nums2:

            while(stk and stk[-1]<i):
                a=stk.pop()
                res[dict1[a]] = i

            if i not in dict1:
                continue
            else:
                
                stk.append(i)

        return res
