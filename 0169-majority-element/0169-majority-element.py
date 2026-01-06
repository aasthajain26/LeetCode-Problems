class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element in an array using Moore's Voting Algorithm.

        The majority element is the element that appears more than ⌊n/2⌋ times.
        If no such element exists, the function returns -1.

        Algorithm:
        1. Candidate Selection Phase:
            - Use a counter (`cnt`) and a candidate (`ele`).
            - Traverse the array:
                - If `cnt` is 0, set the current number as the candidate and initialize `cnt` to 1.
                - If the current number matches the candidate, increase `cnt`.
                - Otherwise, decrease `cnt`.

        2. Verification Phase:
            - Count occurrences of the selected candidate.
            - If it appears more than `n/2` times, return it.
            - Otherwise, return -1.

        Time Complexity: O(n)  
        Space Complexity: O(1)  (Uses constant extra space)

        """
        cnt=0
        el= None

        for i in range(len(nums)):

            if cnt == 0:
                cnt +=1
                el= nums[i]
            elif nums[i] == el:
                cnt +=1
            else:
                cnt -=1
        
        cnt2=0
        for i in nums:
            if i == el:
                cnt2 += 1

        if cnt2 > len(nums) // 2:
            return el
        return -1
