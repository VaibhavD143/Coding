class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        res = 0
        i=1
        while i<len(A):
            st = [A[i-1],B[i-1]]
            dt = [A[i],B[i]]
            
            abX = abs(st[0]-dt[0])
            abY = abs(st[1]-dt[1])
            res+= abs(abX-abY)
            res+= min(abX,abY)
            i+=1
        return res