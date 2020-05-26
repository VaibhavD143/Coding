class Solution:
    def spiralOrder(self, A):
        if not A:
            return []
        if not A[0]:
            return [[]]
        r1,c1=0,0
        r2,c2=len(A)-1,len(A[0])-1
        res=[]
        while r1<r2 and c1<c2:
            #upper row from start to end
            for i in range(c1,c2+1):
                res.append(A[r1][i])
            
            for i in range(r1+1,r2+1):
                res.append(A[i][c2])
            
            for i in range(c2-1,c1,-1):
                res.append(A[r2][i])
            
            for i in range(r2,r1,-1):
                res.append(A[i][c1])
            
            r1,c1=r1+1,c1+1
            r2,c2=r2-1,c2-1
        if r1==r2:
            for i in range(c1,c2+1):
                res.append(A[r1][i])
        elif c1==c2:
            for i in range(r1,r2+1):
                res.append(A[i][c1])
        return res