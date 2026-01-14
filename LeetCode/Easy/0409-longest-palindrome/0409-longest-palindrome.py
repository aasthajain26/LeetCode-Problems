class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict1= {}

        for i in s:
            if i in dict1:
                dict1[i] +=1
            else:
                dict1[i] =1

        cnt = 0 
        for i in dict1:
            if dict1[i] %2 ==0:
                cnt +=dict1[i]
            elif dict1[i] ==1:
                continue
            else:
                cnt += int((dict1[i]-1))
                dict1[i] =1
            
        if len(s) != cnt:
            cnt +=1

        return cnt