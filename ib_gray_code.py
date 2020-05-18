
class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 0:
            return []
        if A == 1:
            return [0,1]
            
        res = [0,1]
        #My Code
        # while A-1:
        #     res = res+res[::-1]
        #     half = len(res)//2
        #     for i in range(half):
        #         res[i]='0'+res[i]
        #         res[i+half]='1'+res[i+half]
        #     A-=1
        # return [int(i,2) for i in res]
        
        #Learnt Code
        for i in range(1,A):
            res += [s|(1<<i) for s in reversed(res)]
        return res