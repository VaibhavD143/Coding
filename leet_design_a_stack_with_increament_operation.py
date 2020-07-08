class CustomStack:

    def __init__(self, maxSize: int):
        self.ss = [None]*maxSize
        self.ind=0

    def push(self, x: int) -> None:
        if self.ind == len(self.ss):
            return
        self.ss[self.ind] = [x,0]
        self.ind+=1
        

    def pop(self) -> int:
        if self.ind == 0:
            return -1
        val = self.ss[self.ind-1][0]+self.ss[self.ind-1][1]
        self.ind-=1
        if self.ind!=0:
            self.ss[self.ind-1][1] += self.ss[self.ind][1]
        return val

    def increment(self, k: int, val: int) -> None:
        if self.ind !=0:
            self.ss[min(k-1,self.ind-1)][1]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)