class Solution:
    def countBits(self, num: int) -> List[int]:
        res=[0]
        while len(res)<=num:
            l = len(res)
            for i in range(l):
                res.append(res[i]+1)
                if len(res)==num+1:
                    break
        return res
    def countBits2(self, num: int) -> List[int]:
        res =[0]
        for i in range(1,num+1):
            res.append( res[i//2] + (i %2 == 1))
        return res