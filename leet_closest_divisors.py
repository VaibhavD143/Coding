class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        num+=1
        for i in range(1+int((num)**0.5),0,-1):
            if num%i == 0:
                diff1 = abs(i-(num//i))
                a,b = i,num//i
                break
        num+=1
        for i in range(1+int((num)**0.5),0,-1):
            if num%i == 0:
                diff2 = abs(i-(num//i))
                a1,b2 = i,(num)//i
                break
        # print(a,b,diff1,a1,b2,diff2)
        return [a,b] if diff1<diff2 else [a1,b2]