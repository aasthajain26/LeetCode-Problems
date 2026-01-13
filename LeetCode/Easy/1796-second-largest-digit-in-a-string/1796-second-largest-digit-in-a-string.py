class Solution:
    def secondHighest(self, s: str) -> int:
        l = -1
        sl = -1

        for i in s:
            if i.isdigit():
                if int(i) > l:
                    sl = l
                    l=int(i)

                elif int(i) <l and int(i) > sl:
                    sl = int(i)

            else:
                continue
        return sl