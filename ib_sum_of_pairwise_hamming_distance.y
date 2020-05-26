import math
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        if not A or not max(A):
            return 0
        i=32
        c1=len(A)
        res=0
        while i:
            # print(i)
            c0=len(A)
            for n in A:
                if n&(1<<(i-1)):
                    c0-=1
            res+=(c0*(len(A)-c0))
            i-=1
        return (res*2)%1000000007
        # def ones(x):
        #     cnt = 0
        #     while x:
        #         cnt+=1
        #         x&=(x-1)
        #     return cnt
        # res=0
        # for i in range(len(A)):
        #     for j in range(i+1,len(A)):
        #         res+=2*ones(A[i]^A[j])
        # return res%1000000007