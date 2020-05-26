class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        A=[[None]*A for _ in range(A)]
        r1,c1=0,0
        r2,c2=len(A)-1,len(A[0])-1
        num=1
        while r1<=r2 and c1<=c2:
            #upper row from start to end
            for i in range(c1,c2+1):
                A[r1][i]=num
                num+=1
            
            for i in range(r1+1,r2+1):
                A[i][c2]=num
                num+=1
            
            for i in range(c2-1,c1,-1):
                A[r2][i]=num
                num+=1
            
            for i in range(r2,r1,-1):
                A[i][c1]=num
                num+=1
            
            r1,c1=r1+1,c1+1
            r2,c2=r2-1,c2-1
        return A