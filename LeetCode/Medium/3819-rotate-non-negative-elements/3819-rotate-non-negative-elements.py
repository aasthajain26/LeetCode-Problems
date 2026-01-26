class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        a=[]
        b=[]
        for i,j in  enumerate(nums):
            if j >= 0 :
                a.append(i)
                b.append(j)

        if not b:
            return nums

        k =k % len(b)
        m =0 
        b = b[k:] + b[:k]

        for i in range(len(a)):

            nums[a[i]] = b[i]

        return nums
        