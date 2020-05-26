import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A==1:
            return 1
        for i in range(2,int(A**0.5)+1):
            
            if i**(int(math.log(A)/math.log(i))) == A:
                return 1
        return 0
        
        #Editorial, dicey
        # for i in range(2,33):
        #     n = round(A**(1/i))
        #     print(1/i,n,n**i)
        #     if n**i == A:
        #         return 1
        # return 0