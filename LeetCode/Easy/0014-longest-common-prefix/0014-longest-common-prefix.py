class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r=""
        for i in range(len(strs[0])):
            for j in strs:
                if i > len(j)-1  or strs[0][i] != j[i]:
                    return r
                
            r += j[i]

        return r

        