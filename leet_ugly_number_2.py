class Ugly:
    def __init__(self):
        self.uglyList = [1,]
        i2 = i3 = i5 = 0
        for _ in range(1,1691):
            nugly = min(self.uglyList[i2]*2,self.uglyList[i3]*3,self.uglyList[i5]*5)
            self.uglyList.append(nugly)
            if nugly == self.uglyList[i2]*2:
                i2+=1
            if nugly == self.uglyList[i3]*3:
                i3+=1
            if nugly == self.uglyList[i5]*5:
                i5+=1


class Solution:
    
    obj = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        
        return self.obj.uglyList[n-1]
obj = Solution()

print(obj.nthUglyNumber(10))
print(obj.nthUglyNumber(4))
print(obj.nthUglyNumber(15))
print(obj.nthUglyNumber(1690))