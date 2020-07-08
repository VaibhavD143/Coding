"""
Intution:
check at every bits and add them as they contribute
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        res=0
        for i in range(32):
            ones = 0
            zeros = 0
            for num in A:
                if num&(1<<i):
                    ones+=1
                else:
                    zeros+=1
            # print(i,ones,zeros)
            res+=(2*ones*zeros)%1000000007
        return res%1000000007
            
        
        #TLE,if memorisation then Memory limit
        # def countOnes(n):
        #     cnt=0
        #     while n:
        #         n=n&(n-1)
        #         cnt+=1
        #     return cnt
        # ha={}
        # res=0
        # for i in range(len(A)):
        #     for j in range(i+1,len(A)):
        #         n = A[i]^A[j]
        #         # if n in ha:
        #         #     res+=(2*ha[n])
        #         # else:
        #         #     ha[n] = countOnes(n)
        #             # res+=(2*ha[n])
        #         res+=(2*countOnes(n))
        #     res%=1000000007
        # return res%1000000007
        
        