class MinStack:
    
    def __init__(self):
        self.a=[]
        self.mini=None

    def push(self, val: int) -> None:
        if not self.a:
            self.mini =val
            self.a.append(val)
            return 
        if val > self.mini:
            self.a.append(val)
        else:
            diff=2*val-self.mini
            self.a.append(diff)
            self.mini=val
        

    def pop(self) -> None:
        if not self.a:
            return
        
        val=self.a.pop()
        if val < self.mini:
            self.mini=2*self.mini -val


    def top(self) -> int:
        if not self.a:
            return -1
        val=self.a[-1]
        if self.mini < val:
            return val
        return self.mini
        

    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()