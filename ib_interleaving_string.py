class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        if len(A)+len(B)!=len(C):
            return 0
        def isPossible(a,b,c,ia,ib,ic):
            # print(A[ia:],B[ib:],C[ic:])
            if ic == len(C):
                if ia==len(A) and ib==len(B):
                    return 1
                return 0
            res=0
            if ia<len(A) and A[ia]==C[ic]:
                res=isPossible(A,B,C,ia+1,ib,ic+1)
            if not res and ib<len(B) and B[ib]==C[ic]:
                res=isPossible(A,B,C,ia,ib+1,ic+1)
            return res
        return isPossible(A,B,C,0,0,0)