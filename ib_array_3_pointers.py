"""
Intution:
Ultimately they are asking for abs(max-min)
and once any array is exhausted, that's the end because afterwards it will only increase the difference
"""
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        a,b,c=0,0,0
        res = float("inf")
        while a<len(A) and b<len(B) and c<len(C):
            minV= min(A[a],B[b],C[c])
            maxV = max(A[a],B[b],C[c])
            diff = abs(maxV-minV)
            res = min(res,diff)
            if minV == A[a]:
                a+=1
            if minV==B[b]:
                b+=1
            if minV == C[c]:
                c+=1
        return res