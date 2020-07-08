class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        def comb(ind,k):
            if k == 0:
                res.append(lst[:])
                return
            if ind>=len(A):
                return
            lst.append(A[ind])
            comb(ind+1,k-1)
            lst.pop()
            comb(ind+1,k)
        
        if A<B or B ==0:
            return []
            
        lst = []
        res = []
        A = list(range(1,A+1))
        comb(0,B)
        return res