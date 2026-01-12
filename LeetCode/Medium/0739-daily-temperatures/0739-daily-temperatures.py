class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        st = []

        for i,e in enumerate(temperatures):

            while st and temperatures[st[-1]] < e:
                v=st.pop()
                res[v] = i - v 
                

            st.append(i)
        return res