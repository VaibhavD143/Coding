"""
gyaan:
abs(A-B) < C then valid set
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A.sort()
        res=0
        for i in range(len(A)-1,-1,-1):
            k=0
            j=i-1
            while j>=0 and j-k > 0:
                while k<j and A[k]<=A[i]-A[j]:
                    k+=1
                res+=(j-k)
                j-=1
        return res%1000000007
            