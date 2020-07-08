import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            tres=0
            cnt=0
            for i in range(1,1+int(math.sqrt(n))):
                if n%i==0:
                    if i*i == n:
                        cnt=5
                        break
                    tres+=i
                    tres+=(n//i)
                    cnt+=1
                    if cnt ==3:
                        break
            if cnt==2:
                res+=tres
        return res