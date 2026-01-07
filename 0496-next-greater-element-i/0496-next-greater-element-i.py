class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dict1={}
        for i, j in enumerate(nums1):
            dict1[j]=i

        res =[-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i]  not in  dict1:
                continue
            else:
                for j in range(i+1, len(nums2)):
                    if nums2[j]> nums2[i]:
                        ind = dict1[nums2[i]]
                        res[ind] = nums2[j]
                        break


        
        return res


