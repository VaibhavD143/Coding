class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        aXb = 0
        for n in nums:
            aXb ^=n
        
        diff = aXb&-aXb
        
        w,wo=[],[]
        for n in nums:
            if n&diff:
                w.append(n)
            else:
                wo.append(n)
        a = 0
        for n1 in w:
            a^=n1
        b = a^aXb
        return a,b